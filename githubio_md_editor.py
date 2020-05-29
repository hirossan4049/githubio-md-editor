import browser
from browser import timer
from browser import ajax, window, load
from javascript import JSConstructor, JSObject
from browser import markdown

# load("save_md.js")

test_md = """
# markdown test!
markdown test!

- [ ] checkbox!
- [x] checkedbox!

## h2

```py
import this
print("hello world!")
```

```java
public void test(View v){
    textView.setText("hello world!")
}
```
"""
# browser.document["markdown-input"].value = test_md


# browser.document.open()
# browser.document.write("hello")
# browser.document.close()

# def read(f):
#     data = f.read()
#     assert isinstance(data, bytes)
#
# req = ajax.get("tests.zip", mode="binary",
#     oncomplete=read)

# ===== MARKDOWN =========
# mk, scripts = markdown.mark("""# Helloworld!
# ```py
# import this
#
# prinnt('hello world!')""")
#
# browser.document["debug-print"].text = mk
# ========================

def debug_print(string):
    browser.document["debug-print"].text += "\n\n***" + str(string) + "***\n\n"


def get_md():
    return browser.document["markdown-input"].value


def ganbattazolo():
    # a = browser.document.createElement("A")
    # createUrl = window.URL.createObjectURL
    # createUrl = JSObject(window.URL.createObjectURL)
    # blob = JSConstructor(window.Blob)
    # blob = window.Blob.new
    # blob("hello world!", {"type": "text/plain"})
    # a.href = createUrl(req)
    # a.download = "ikemen.txt"
    # a.click()
    # import markdown.core
    # browser.document["debug-print"].text = "PYTHON COMPLATED!" + str(a)
    # text = "None"
    pass


def get_cookie(arg):
    cookies = browser.document.cookie.split(";")
    print("cookies:",cookies)
    for item in cookies:
        sp = item.split("=")
        if sp[0].strip() == arg:
            return sp[1]


def draw_markdown():
    # mk, scripts = markdown.mark(get_md())
    mk = window.marked(get_md())
    browser.document["markdown-result"].html = mk
    encodeURIComponent = JSObject(window.encodeURIComponent)
    browser.document.cookie = "markdown={md}".format(md=encodeURIComponent(get_md()))
timer.set_interval(draw_markdown, 100)


def markdown_change(ev):
    debug_print("inpt")
    print(browser.document.cookie)
    draw_markdown()

    # window.download_md(get_md())
    # browser.document["markdown-code"].text = browser.document["markdown-input"].value
    debug_print("done")



# import time
# index = 0
# def test_timer():
#     global index
#     index += 1
#     browser.document["debug-print"].text = str(index)
#
# timer.set_interval(test_timer, 10)

browser.document["markdown-change"].bind("click", markdown_change)
browser.document["markdown-input"].value = JSObject(window.decodeURIComponent)(get_cookie("markdown"))
