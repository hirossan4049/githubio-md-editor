// let text = document.getElementById("markdown-code").textContent

function download_md(text) {
    var blob = new Blob(
        [text],
        {"type": "text/plain"})
    let link = document.createElement('a')
    link.href = window.URL.createObjectURL(blob)
    link.download = 'markdown.md'
    link.click()
}