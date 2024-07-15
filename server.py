from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import AnyUrl
from browserstack.utils import open_tab, close_browser, active_tab, browser_cleanup

app = FastAPI()

template = Jinja2Templates(directory="templates")


@app.get("/start/", response_class=HTMLResponse)
def start_browser(browser: str, url: AnyUrl, request: Request):
    context = {"message": ""}
    context["message"] = open_tab(browser, str(url))
    return template.TemplateResponse(
        request=request, name="index.html", context=context
    )


@app.get("/stop/", response_class=HTMLResponse)
def stop_browser(browser: str, request: Request):
    context = {"message": ""}
    context["message"] = close_browser(browser)
    return template.TemplateResponse(
        request=request, name="index.html", context=context
    )


@app.get("/geturl/", response_class=HTMLResponse)
def get_active_tab_url(browser: str, request: Request):
    context = {"message": "", "link": "", "link_text": ""}
    context["message"], context["link"], context["link_text"] = active_tab(browser)
    return template.TemplateResponse(
        request=request, name="index.html", context=context
    )


@app.get("/cleanup/", response_class=HTMLResponse)
def cleanup(browser: str, request: Request):
    context = {"message": ""}
    context["message"] = browser_cleanup(browser)
    return template.TemplateResponse(
        request=request, name="index.html", context=context
    )
