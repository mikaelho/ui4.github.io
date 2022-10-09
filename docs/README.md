Are you looking to create a web application instead of a document?
Is CSS with its multiple layout engines too complicated for your needs? 

ui4 provides an alternative for placing UI elements on the screen. Let's look at some examples:

#### "Connect this to the corner"


<table class="example">
  <tr>
    <td>
      <sub>EXAMPLE 1</sub>
      
```html
<div id="square" top="root.top" left="root.left"></div>
```
    </td>
    <td>
      <iframe style="border-style:none;box-shadow:0px 0px 2px 2px rgba(0,0,0,0.2);" src="examples/example0001.html"></iframe><br/>
      <button onclick="location.href='examples/example0001.html'">Open in full screen</button>
    </td>
  </tr>
</table>

Pretty close to CSS `top` or `left`, just with the little gaps added between the element and the
edges of the parent.

In addition to `top` and `left`, you can also use `bottom`, `right`, `width`, `height`, `centerx`
and `centery`.

#### "Connect A to B"


<table class="example">
  <tr>
    <td>
      <sub>EXAMPLE 2</sub>
      
```html
<div id="b" top="root.top" left="root.left">B</div>
<div id="a" top="b.bottom" left="b.left">A</div>
```
    </td>
    <td>
      <iframe style="border-style:none;box-shadow:0px 0px 2px 2px rgba(0,0,0,0.2);" src="examples/example0002.html"></iframe><br/>
      <button onclick="location.href='examples/example0002.html'">Open in full screen</button>
    </td>
  </tr>
</table>

Same `top` and `left` work with peer elements in an intuitive way, "pushing" against them instead
of aligning with the edge.

#### "I want them closer"


<table class="example">
  <tr>
    <td>
      <sub>EXAMPLE 3</sub>
      
```html
<div id="b" top="root.top" left="root.left">B</div>
<div id="a" top="b.bottom-(gap-1)" left="b.left">A</div>
```
    </td>
    <td>
      <iframe style="border-style:none;box-shadow:0px 0px 2px 2px rgba(0,0,0,0.2);" src="examples/example0003.html"></iframe><br/>
      <button onclick="location.href='examples/example0003.html'">Open in full screen</button>
    </td>
  </tr>
</table>

Simple math is available, including `min` and `max`. `gap` is by default 8 (px). In the example it
is used to make sure there is only 1 pixel between A and B, no matter what the gap has been set to.

#### "Just put it in the center"


<table class="example">
  <tr>
    <td>
      <sub>EXAMPLE 4</sub>
      
```html
<div id="centered" dock="center"></div>
```
    </td>
    <td>
      <iframe style="border-style:none;box-shadow:0px 0px 2px 2px rgba(0,0,0,0.2);" src="examples/example0004.html"></iframe><br/>
      <button onclick="location.href='examples/example0004.html'">Open in full screen</button>
    </td>
  </tr>
</table>

Instead of using the primitives (like `centerx` and `centery` in this case), `dock` provides
convenient and easier to read options.

#### "This is a top banner"


<table class="example">
  <tr>
    <td>
      <sub>EXAMPLE 5</sub>
      
```html
<div id="topBanner" dock="top" height="30"></div>
```
    </td>
    <td>
      <iframe style="border-style:none;box-shadow:0px 0px 2px 2px rgba(0,0,0,0.2);" src="examples/example0005.html"></iframe><br/>
      <button onclick="location.href='examples/example0005.html'">Open in full screen</button>
    </td>
  </tr>
</table>

Docking to the top connects the left, top and right edges of the element; bottom or height is set
separately.

All the options for docking to the parent are:
- `top`, `left`, `right`, `bottom`
- `topleft`, `topright`, `bottomleft`, `bottomright`
- `topcenter`, `leftcenter`, `rightcenter`, `bottomcenter`
- `all`

#### "Put A above B"


<table class="example">
  <tr>
    <td>
      <sub>EXAMPLE 6</sub>
      
```html
<div id="b" dock="center" width="50" height="30">B</div>
<div id="a" dock="b.above" height="30">A</div>
```
    </td>
    <td>
      <iframe style="border-style:none;box-shadow:0px 0px 2px 2px rgba(0,0,0,0.2);" src="examples/example0006.html"></iframe><br/>
      <button onclick="location.href='examples/example0006.html'">Open in full screen</button>
    </td>
  </tr>
</table>

These convenience docking options, `above`, `below`, `rightof` and `leftof`, place the element
beside another one and set the shared dimension (width in the example above) to be the same.

#### "This is a third of the size of the whole thing"


<table class="example">
  <tr>
    <td>
      <sub>EXAMPLE 7</sub>
      
```html
<div id="one_third" dock="left" width="share(1, 3)"></div>
```
    </td>
    <td>
      <iframe style="border-style:none;box-shadow:0px 0px 2px 2px rgba(0,0,0,0.2);" src="examples/example0007.html"></iframe><br/>
      <button onclick="location.href='examples/example0007.html'">Open in full screen</button>
    </td>
  </tr>
</table>

Because of the gaps, just dividing the width by 3 is not accurate, so we use a convenience function
for getting "gap-observing" shares of the whole.

Place this div between A and B: