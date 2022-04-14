from manimlib import *


class BubbleSort(Scene):
    def construct(self) -> None:
        title = Text("经典排序算法之冒泡排序")
        self.play(ShowCreation(title))
        self.wait(1)
        self.remove(title)

        step_title = Text("算法步骤")
        step_title.to_edge(UP)
        self.play(ShowCreation(step_title))

        step_text = ["比较相邻的元素。如果第一个比第二个大，就交换他们两个",
                     "对每一对相邻元素作同样的工作\n从开始第一对到结尾的最后一对",
                     "针对所有的元素重复以上的步骤\n直到没有任何一对数字需要比较"
                     ]
        for text in step_text:
            step = Text(text)
            self.play(ShowCreation(step))
            self.wait(2)
            self.remove(step)

        self.remove(step_title)

        complexity_tex = Tex("\\mathcal{O}(n^2)")
        complexity_text = Text("时间复杂度")
        complexity_tex.next_to(complexity_text, buff=0.4)

        complexity = VGroup(complexity_text, complexity_tex)

        self.play(ShowCreation(complexity))
        self.wait(1)
        self.remove(complexity)

        show = Text("动画演示")
        show.to_edge(UP)
        self.play(ShowCreation(show))

        color = [GREEN, PURPLE, ORANGE, BLUE, PINK, MAROON, TEAL]
        sort_list = [8, 5, 7, 2, 1, 4, 3]
        rect_list = []
        for i in range(len(sort_list)):
            text = Text(str(sort_list[i]))
            rect = VGroup(
                Rectangle(width=1, height=sort_list[i] / 2, color=color[i], fill_color=color[i], fill_opacity=.5), text)

            if i != 0:
                last = rect_list[i - 1]
                rect.next_to(last, RIGHT, buff=1)
                rect.align_to(last, DOWN)

            rect_list.append(rect)

        g = VGroup(*rect_list)
        g.center()
        self.play(ShowCreation(g))
        self.wait(1.5)

        sort_brace = None
        sort_len = len(sort_list)
        for i in range(1, sort_len):
            for j in range(0, sort_len - i):
                if sort_brace:
                    self.remove(sort_brace)
                sort_group = VGroup(rect_list[j], rect_list[j + 1])

                if sort_list[j] > sort_list[j + 1]:
                    sort_brace = BraceText(sort_group, "")
                    self.add(sort_brace)
                    self.wait(1)

                    sort_list[j], sort_list[j + 1] = sort_list[j + 1], sort_list[j]
                    rect_list[j], rect_list[j + 1] = rect_list[j + 1], rect_list[j]

                    self.play(rect_list[j].animate.shift(2 * LEFT))
                    self.play(rect_list[j + 1].animate.shift(2 * RIGHT))
                else:
                    sort_brace = BraceText(sort_group, "")
                    self.add(sort_brace)
                    self.wait(1)
