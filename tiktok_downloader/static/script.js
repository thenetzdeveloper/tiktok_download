async function downloadVideo() {
    const url = document.getElementById("tiktokUrl").value;
    const resultDiv = document.getElementById("result");
    resultDiv.innerHTML = "<p>កំពុងដំណើរការដោនឡូត...</p>";
    const response = await fetch("/download", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ url })
    });
    const data = await response.json();
    if (data.success) {
        resultDiv.innerHTML = `
        <video controls width="320">
        <source src="${data.video}" type="video/mp4">
        </video>
    <p>
    <a href="/download_file?video_url=${encodeURIComponent(data.video)}" target="_blank" class="download-button">
    ទាញយកវីដេអូ</a>
    </p>
`;
    } else {
        resultDiv.innerHTML = `<p style="color:red;">${data.error}</p>`;
    }
}