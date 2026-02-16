# Markdown to HTML compiler

![](https://github.com/mikeizbicki/markdown-compiler/workflows/doctests/badge.svg)&nbsp;
![](https://github.com/mikeizbicki/markdown-compiler/workflows/flake8/badge.svg)&nbsp;
![](https://github.com/mikeizbicki/markdown-compiler/workflows/command_line/badge.svg)&nbsp;

A simple project for converting markdown files to HTML.

Basic usage:
```
$ markdown-compiler example/README.md
```
![](examples/example1.png)

Fancy CSS formatting can be included with the flag `--add_css`:
```
$ markdown-compiler example/README.md --add_css
```
![](examples/example2.png)
