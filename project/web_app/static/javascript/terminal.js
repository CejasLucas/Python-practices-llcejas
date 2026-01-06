document.addEventListener("DOMContentLoaded", () => {
    // =====================================
    // Terminal configuration
    // =====================================
    const term = new Terminal({
        theme: {
            background: '#0b0e14',
            foreground: '#FEFEFE',
            cursor: '#00D1B2'
        },
        fontFamily: 'JetBrains Mono, monospace',
        fontSize: 14,
        lineHeight: 1.2,
        cursorBlink: true,
        scrollback: 2000 // IMPORTANT for scrolling
    });

    const fitAddon = new FitAddon.FitAddon();
    term.loadAddon(fitAddon);

    const socket = io();
    const terminalDiv = document.getElementById("terminal");

    if (!terminalDiv) {
        console.error("Error: #terminal div not found");
        return;
    }

    term.open(terminalDiv);
    fitAddon.fit();
    term.refresh(0, term.rows - 1);

    // Recalculate on window resize
    window.addEventListener("resize", () => {
        fitAddon.fit();
    });

    // =====================================
    // Exercise data validation
    // =====================================
    if (!window.exerciseData) {
        console.error("exerciseData is not defined");
        return;
    }

    const { folderName, moduleId, exerciseId } = window.exerciseData;

    // Initial message
    term.write(`📂  Loading the practice ${folderName} exercises.\r\n`);

    socket.emit("start_exercise", {
        folder_name: folderName,
        exercise_id: exerciseId
    });

    // =====================================
    // Input state
    // =====================================
    let buffer = "";
    let exerciseFinished = false;

    // =====================================
    // Terminal input handling
    // =====================================
    term.onData(data => {
        for (const char of data) {

            // If the exercise is finished, ENTER closes the popup
            if (exerciseFinished && char === "\r") {
                closePopup();
                return;
            }

            // Normal input behavior
            if (char === "\r") {
                socket.emit("input", buffer);
                buffer = "";
                term.write("\r\n");
            }
            else if (char === "\u007F") {
                // Handle backspace
                if (buffer.length > 0) {
                    buffer = buffer.slice(0, -1);
                    term.write("\b \b");
                }
            }
            else {
                buffer += char;
                term.write(char);
            }
        }
    });

    // =====================================
    // Socket events
    // =====================================
    socket.on("output", data => {
        term.write(data, () => {
            term.scrollToBottom();
        });
    });

    socket.on("end", () => {
        exerciseFinished = true;

        term.write("\r\n🎉 Exercise finished\r\n");
        term.write("↩️ Press ENTER to continue...\r\n");
        term.scrollToBottom();
    });

    socket.on("graph", data => {
        localStorage.setItem("lastGraph", data);
        const urlDiv = document.getElementById("url");

        if (urlDiv) {
            urlDiv.innerHTML = "";

            const link = document.createElement("a");
            link.href = "/graphic";
            link.target = "_blank";
            link.textContent = "🔗 See generated graph";

            urlDiv.appendChild(link);
            term.write("\r\n[INFO] Click the link on the right to open it.\r\n");
        }
    });

    // =====================================
    // Close popup logic (ENTER only)
    // =====================================
    function closePopup() {
        const overlay = document.getElementById("overlay");
        if (!overlay) return;

        overlay.style.opacity = 0;

        setTimeout(() => {
            overlay.style.display = "none";
            window.location.href = `/module/${moduleId}`;
        }, 300);
    }
});
