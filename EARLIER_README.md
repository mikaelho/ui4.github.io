Natural layouts for web UIs
===========================

CSS does a fair job with styling things, but layouts with it are always a bit hit and miss.
ui4.html provides layout management straight in the HTML, sharing some of the philosophy of locality
with the likes of HTMX and Tailwind CSS.

ui4 treats the HTML document as a fixed-screen canvas, and not an eternally scrolling document.

For convenience and less code, a number of shortcuts like `dock=center` are available.

Table test:

<table>
<tr>
<td>
<pre lang="html">&lt;div id="foo">&lt;/div></pre>
</td>
</tr>
</table>

# Primitives

You can place elements precisely but flexibly with a set of layout primitives: `left`/`x`, `top`/`y`, `right`, `bottom`, `centerx`, `centery`, `width`, `height`.

You use them in HTML elements using the `ui4` attribute:

```html
<div id="root">
  <input id="searchText" ui4="left=root.left; top=root.top; right=searchButton.left">
  <button id="searchButton" ui4="top=root.top; right=root.right;">Search</button>
</div>
```

If you prefer, you can split the `ui4` attribute into several attributes, which raises namespace concerns but can be more readable with typical code highlighting:

```html
<input id="searchText" left="root.left" top="root.top" right="searchButton.left">
```


```html
<div id="root" class="ui4Root">
    <input id="searchField"
           ui4="dock=topLeft; right=left.searchButton; height=height.searchButton;"
           class="form-control block px-3 py-1.5 text-base font-normal text-gray-700 bg-white bg-clip-padding border border-solid border-gray-300 rounded focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none">
    <button id="searchButton"
            ui4="dock=topRight; width=100"
            class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 border border-blue-700 rounded">
        Search
    </button>
    <div id="resultArea"
         ui4="top=bottom.searchField; dock=sides; bottom=top.buttonArea+gap;"
         class="border border-solid border-gray-300 rounded bg-gradient-to-br from-white to-blue-100">
        <div id="resultPlaceholder"
             ui4="dock=center"
             class="text-base font-normal text-gray-700">
            Results will appear here
        </div>
    </div>
    <div id="buttonArea" ui4="fit=true; centerX=centerX.root; bottom=bottom.root+gap;">
        <button id="selectButton" ui4="dock=topLeft; width=width.searchButton;"
                class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 border border-blue-700 rounded">
            Done
        </button>
        <button id="cancelButton"
                ui4="dock=rightOf.selectButton; width=width.searchButton"
                class="bg-transparent hover:bg-blue-500 text-blue-700 font-semibold hover:text-white py-2 px-4 border border-blue-500 hover:border-transparent rounded">
            Cancel
        </button>
    </div>
</div>
```

<html>
<head>
    <meta charset="utf-8">

    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no"/>

    <title>ui4 Playground</title>
    <script src="ui4.js"></script>
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body>
<div id="root" class="ui4Root">
    <input id="searchField"
           ui4="dock=topLeft; right=left.searchButton; height=height.searchButton;"
           class="form-control block px-3 py-1.5 text-base font-normal text-gray-700 bg-white bg-clip-padding border border-solid border-gray-300 rounded focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none">
    <button id="searchButton"
            ui4="dock=topRight; width=100"
            class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 border border-blue-700 rounded">
        Search
    </button>
    <div id="resultArea"
         ui4="top=bottom.searchField; dock=sides; bottom=top.buttonArea+gap;"
         class="border border-solid border-gray-300 rounded bg-gradient-to-br from-white to-blue-100">
        <div id="resultPlaceholder"
             ui4="dock=center"
             class="text-base font-normal text-gray-700">
            Results will appear here
        </div>
    </div>
    <div id="buttonArea" ui4="fit=true; centerX=centerX.root; bottom=bottom.root+gap;">
        <button id="selectButton" ui4="dock=topLeft; width=width.searchButton;"
                class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 border border-blue-700 rounded">
            Done
        </button>
        <button id="cancelButton"
                ui4="dock=rightOf.selectButton; width=width.searchButton"
                class="bg-transparent hover:bg-blue-500 text-blue-700 font-semibold hover:text-white py-2 px-4 border border-blue-500 hover:border-transparent rounded">
            Cancel
        </button>
    </div>
</div>
</body>
</html>


