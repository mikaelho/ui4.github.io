Are you looking to create a web application instead of a document?
Is CSS with its multiple layout engines too complicated for your needs? 

ui4 provides an alternative for placing UI elements on the screen. Let's look at some examples:

#### "Connect this to the corner"


<table>
  <tr>
    <td>
      <sub>EXAMPLE 1</sub>
      <pre>&lt;div id="square" top="root.top" left="root.left">&lt;/div></pre>
    </td>
    <td>
      <iframe style="border-style:none;box-shadow:0px 0px 2px 2px rgba(0,0,0,0.2);" src="examples/example0001.html"></iframe>
      <button onclick="location.href='examples/example0001.html'">Open in full screen</button>
    </td>
  </tr>
</table>

Pretty close to CSS `top` or `left`, just with the little gaps added between the element and the
edges of the parent.

In addition to `top` and `left`, you can also use `bottom`, `right`, `width`, `height`, `centerx`
and `centery`.

#### "Connect A to B"


<table>
  <tr>
    <td>
      <sub>EXAMPLE 2</sub>
      <pre>&lt;div id="b" top="root.top" left="root.left">B&lt;/div>
&lt;div id="a" top="b.bottom" left="b.left">A&lt;/div></pre>
    </td>
    <td>
      <iframe style="border-style:none;box-shadow:0px 0px 2px 2px rgba(0,0,0,0.2);" src="examples/example0002.html"></iframe>
      <button onclick="location.href='examples/example0002.html'">Open in full screen</button>
    </td>
  </tr>
</table>

Same `top` and `left` work with peer elements in an intuitive way, "pushing" against them instead
of aligning with the edge.

#### "Just put it in the center"


<table>
  <tr>
    <td>
      <sub>EXAMPLE 3</sub>
      <pre>&lt;div id="centered" dock="center">&lt;/div></pre>
    </td>
    <td>
      <iframe style="border-style:none;box-shadow:0px 0px 2px 2px rgba(0,0,0,0.2);" src="examples/example0003.html"></iframe>
      <button onclick="location.href='examples/example0003.html'">Open in full screen</button>
    </td>
  </tr>
</table>

Instead of using the primitives (like `centerx` and `centery` in this case), `dock` provides
convenient and easier to read options.

#### "This is a top banner"


<table>
  <tr>
    <td>
      <sub>EXAMPLE 4</sub>
      <pre>&lt;div id="topBanner" dock="top" height="30">&lt;/div></pre>
    </td>
    <td>
      <iframe style="border-style:none;box-shadow:0px 0px 2px 2px rgba(0,0,0,0.2);" src="examples/example0004.html"></iframe>
      <button onclick="location.href='examples/example0004.html'">Open in full screen</button>
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


<table>
  <tr>
    <td>
      <sub>EXAMPLE 5</sub>
      <pre>&lt;div id="b" dock="center" width="50" height="30">&lt;/div>
&lt;div id="a" dock="b.above" height="30">&lt;/div></pre>
    </td>
    <td>
      <iframe style="border-style:none;box-shadow:0px 0px 2px 2px rgba(0,0,0,0.2);" src="examples/example0005.html"></iframe>
      <button onclick="location.href='examples/example0005.html'">Open in full screen</button>
    </td>
  </tr>
</table>

These convenience docking options, `above`, `below`, `rightof` and `leftof`, place the element
besides another one and set the shared dimension (width in the example above) to be the same.

Place this div between A and B: