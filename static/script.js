document.addEventListener("DOMContentLoaded", () => {
    const sendBtn = document.getElementById("send");
    const input = document.getElementById("input");
    const chatBox = document.getElementById("chat-box");

    sendBtn.addEventListener("click", async () => {
        const message = input.value.trim();
        if (!message) return;

        appendMessage("You", message, "user");
        input.value = "";

        const res = await fetch("/chat", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ message })
        });
        const data = await res.json();
        appendMessage("Bot", data.response, "bot");
    });

    function appendMessage(sender, text, className) {
        const div = document.createElement("div");
        div.classList.add("msg");
        div.innerHTML = `<span class="${className}">${sender}:</span> ${text}`;
        chatBox.appendChild(div);
        chatBox.scrollTop = chatBox.scrollHeight;
    }
});
