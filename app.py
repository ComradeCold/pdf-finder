from flask import Flask, request, render_template
import os
from ddgs import DDGS

app = Flask(__name__)

def duckduckgo_pdf_search(query, num_results=10):
    """Searches for PDF files using DuckDuckGo."""
    try:
        full_query = f"{query} filetype:pdf"
        with DDGS() as ddgs:
            # .text() returns a list of result dictionaries
            results = ddgs.text(
                full_query,
                region="wt-wt",
                safesearch="moderate",
                max_results=num_results
            )
            # DDGS uses 'href' for the URL key
            return [item["href"] for item in results if item.get("href", "").endswith(".pdf")]
    except Exception as e:
        return {"error": f"DuckDuckGo search error: {e}"}

@app.route("/", methods=["GET", "POST"])
def home():
    pdfs = []
    query = ""
    error_message = None

    if request.method == "POST":
        try:
            query = request.form.get("query", "").strip()
            if query:
                result = duckduckgo_pdf_search(query)
                if isinstance(result, dict):
                    error_message = result["error"]
                else:
                    pdfs = result
            else:
                error_message = "Please enter a search term."
        except Exception as e:
            error_message = f"Internal server error: {e}"

    if error_message:
        return render_template("error.html", error_message=error_message)

    return render_template("index.html", pdfs=pdfs, query=query)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
