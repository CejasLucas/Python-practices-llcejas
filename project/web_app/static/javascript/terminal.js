document.addEventListener("DOMContentLoaded", () => {

    const term = new Terminal({
        theme: { background: '#0A0A0A', foreground: '#FEFEFE', cursor: '#00D1B2' },
        fontFamily: 'Fira Mono, monospace',
        fontSize: 14
    });

    const socket = io();
    const terminalDiv = document.getElementById('terminal');
    if (!terminalDiv) return console.error("Error: #terminal div not found");
    term.open(terminalDiv);


    const fileName = window.exerciseData?.fileName || "example.txt";
    const exerciseId = window.exerciseData?.exerciseId || 0;
    term.write(`📂  Loading the practice ${fileName} exercises.\r\n`);


    let inputBuffer = "";
    let finished = false;
    socket.emit("start_exercise", { file_name: fileName, exercise_id: exerciseId });
    term.prompt = () => { term.write("\r\n"); };


    term.onData(e => {
        if (finished) {
            if (e === '\r') closePopup();
            return;
        }
        if (e === '\r') {
            socket.emit("input", inputBuffer);
            term.write("\r\n");
            inputBuffer = "";
        } else if (e === '\u007F') {
            if (inputBuffer.length > 0) {
                inputBuffer = inputBuffer.slice(0, -1);
                term.write('\b \b');
            }
        } else {
            inputBuffer += e;
            term.write(e);
        }
    });

    socket.on("output", data => {
        term.write(data);
        term.prompt();
    });

    socket.on("end", () => {
        finished = true;
        term.write("\r\n🎉  Exercise finished. Press Enter or Close button.\r\n");
        const closeBtn = document.getElementById("close-btn");
        if (closeBtn) closeBtn.style.display = "inline-block";
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
            term.write("\r\n[INFO] Click the link below right to open it.\r\n");
        }
    });

    function closePopup() {
        const overlay = document.getElementById("overlay");
        overlay.style.opacity = 0;
        setTimeout(() => {
            overlay.style.display = "none";
            const fileName = window.exerciseData?.fileName || "";
            window.location.href = `/module/${fileName}`;
        }, 300);
    }

    const closeBtn = document.getElementById("close-btn");
    if (closeBtn) closeBtn.addEventListener("click", closePopup);
});