document.addEventListener("DOMContentLoaded", () => {
    if (!window.exerciseData) {
        console.error("exerciseData no definido");
        return;
    }

    const { folderName, moduleId, exerciseId} = window.exerciseData;

    const term = new Terminal({
        theme: { background: "#000000", foreground: "#ffffff" },
        fontSize: 14
    });

    term.open(document.getElementById("terminal"));

    const socket = io();

    // ✅ CLAVE: esperar conexión
    socket.on("connect", () => {
        socket.emit("start_exercise", {
            folder_name: folderName,
            exercise_id: exerciseId
        });
    });

    let buffer = "";

    term.onData(e => {
        if (e === "\r") {
            socket.emit("input", buffer);
            buffer = "";
            term.write("\r\n");
        } else if (e === "\u007F") {
            buffer = buffer.slice(0, -1);
            term.write("\b \b");
        } else {
            buffer += e;
            term.write(e);
        }
    });

    socket.on("output", data => term.write(data));

    socket.on("end", () => {
        term.write("\r\n✔ Ejercicio terminado\r\n");
        document.getElementById("close-btn").style.display = "block";
    });

    document.getElementById("close-btn").onclick = () => {
        window.location.href = `/module/${moduleId}`;
    };
});
