# HTML & CSS3 Kvikun

```HTML
<div class="kvikun"></div>
```
### CSS

```CSS
.kvikun {
  width: 100px;
  height: 100px;
  background-color: red;
  position: relative;
  animation-name: example;
  animation-duration: 4s;
  animation-iteration-count: infinite;
}

@keyframes example {
  0%   {background-color:red; left:0px; top:0px;}
  25%  {background-color:yellow; left:200px; top:0px;}
  50%  {background-color:blue; left:200px; top:200px;}
  75%  {background-color:green; left:0px; top:200px;}
  100% {background-color:red; left:0px; top:0px;}
}
```

[ANIMATION](https://www.w3schools.com/cssref/css3_pr_animation.asp)

| Value  |  Description |
| ---- | ---- |
| animation-name: | Specifies the name of the keyframe you want to bind to  the selector   |
| animation-duration  | Specifies how many seconds or milliseconds an animation takes to complete  |
| animation-timing-function	| Specifies the speed curve of the animation  |
| animation-delay  | Specifies a delay before the animation will start  |
| animation-iteration-count	| Specifies how many times an animation should be played  |
| animation-direction  | Specifies whether or not the animation should play in reverse on alternate cycles  |
| animation-fill-mode  | Specifies what values are applied by the animation outside the time it is executing  |
| animation-play-state  | Specifies whether the animation is running or paused  |

**Animation** is actually a shorthand for eight subproperties:

`animation: name duration timing delay iteration direction fill play;`

As you're using the shorthand, there's no need to list the subproperties – you just need to define the values you need. You don't need to use all of the subproperties, but animation-name and animation-duration are necessary for the CSS animation property to work as intended.

Note: for the shorthand to work properly, make sure you list the values in the same order as listed above.

* [Sýnidæmi](animation-examples/)
