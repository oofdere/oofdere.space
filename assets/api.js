let quote;

fetch("https://api.oofdere.space/quote")
    .then(response => response.json())
    .then(quote => updateQuote(quote))

function updateQuote(quote) {
    console.log(quote)
    document.getElementById("api-quote").innerHTML = quote.quote;
    if (quote.url != null) {
        let current = document.getElementById("api-quote").innerHTML;
        let anchor = "<a href=\"" + quote.url + "\">" + current + "</a>"
        console.log(anchor)
        document.getElementById("api-quote").innerHTML = anchor;
    }
    if (quote.attrib != null) {
        document.getElementById("api-quote-attrib").innerHTML = quote.attrib;
    }
}