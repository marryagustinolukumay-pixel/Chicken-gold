<!DOCTYPE html>
<html>
<head>
<title>Candy Crush Rahisi</title>
<style>
body {background:#2d1b4e; display:flex; justify-content:center; align-items:center; height:100vh; margin:0; font-family:Arial;}
#game {text-align:center;}
#board {display:grid; grid-template-columns:repeat(8, 50px); gap:4px; margin:20px auto;}
.candy {width:50px; height:50px; border-radius:12px; cursor:pointer; font-size:30px; display:flex; align-items:center; justify-content:center; transition:0.2s;}
.candy:active {transform:scale(0.9);}
.score {color:white; font-size:24px; margin-bottom:10px; font-weight:bold;}
</style>
</head>
<body>
<div id="game">
<div class="score">Alama: <span id="score">0</span></div>
<div id="board"></div