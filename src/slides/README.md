# 课件源文件

本目录只保存可维护的课件源文件与构建入口。

- `lectures-14-beamer/`：14 讲细分版 LaTeX Beamer 源文件、共享样式与逐讲补充示例。
- `Makefile`：将 14 讲正式导出到 `build/slides/2027/lectures-14-beamer/`，并将课程导论补充讲义导出到 `build/slides/handouts/`。

8 讲主课程与中英文课程介绍目前以经过质检的 PPTX 作为正式维护件，分别位于 `build/slides/2027/lectures-8-pptx/` 与 `build/slides/2027/course-overview/`。

构建全部 Beamer 课件：

```sh
make
```

只查看将参与构建的源文件：

```sh
make list
```
