from manimlib import *


class SelectSort(Scene):
    def construct(self) -> None:
        MIN_TEXT = "min"
        SORTED_TEXT = "已排好序"

        title = Text("经典排序算法之选择排序")
        self.play(ShowCreation(title))
        self.wait(1)
        self.remove(title)

        step_title = Text("算法步骤")
        step_title.to_edge(UP)
        self.play(ShowCreation(step_title))

        step_text = ["首先在未排序序列中找到最小（大）元素\n存放到排序序列的起始位置",
                     "再从剩余未排序元素中继续寻找最小（大）元素\n然后放到已排序序列的末尾",
                     "重复上一步\n直到所有元素均排序完毕"
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

        complexity.to_edge(UP)

        self.play(ShowCreation(complexity))

        code_text = '''
        def selection_sort(arr):
          for i in range(len(arr) - 1):
            min_index = i
            for j in range(i + 1, len(arr)):
                if arr[j] < arr[min_index]:
                    min_index = j
            if i != min_index:
                arr[i], arr[min_index] = arr[min_index], arr[i]
          return arr
                '''
        rendered_code = Code(code=code_text, tab_width=2, line_spacing=1,
                             language="Python", font="Monospace")
        rendered_code.to_edge(LEFT)
        self.add(rendered_code)

        sum_tex = Tex("\\sum\\limits_{i=1}^{n-1}i=\\frac{1}{2}(n^2-n)")
        sum_tex.to_edge(RIGHT)
        self.play(ShowCreation(sum_tex))

        self.wait(2)

        self.remove(rendered_code)
        self.remove(sum_tex)
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

        sorted_rect_list = []
        sorted_brace = None
        min_text = None

        for i in range(len(sort_list) - 1):
            min_index = i

            if min_text:
                self.remove(min_text)
            min_text = Text(MIN_TEXT)
            min_text.next_to(rect_list[min_index], DOWN)
            self.play(ShowCreation(min_text))

            for j in range(i + 1, len(sort_list)):
                self.play(WiggleOutThenIn(rect_list[j]))

                if sort_list[j] < sort_list[min_index]:
                    min_index = j
                    if min_text:
                        self.remove(min_text)
                    min_text = Text(MIN_TEXT)
                    min_text.next_to(rect_list[min_index], DOWN)
                    self.play(ShowCreation(min_text))

            if i != min_index:
                sort_list[i], sort_list[min_index] = sort_list[min_index], sort_list[i]

                if min_text:
                    self.remove(min_text)

                self.play(rect_list[i].animate.shift((min_index - i) * RIGHT * 2))
                self.play(rect_list[min_index].animate.shift((min_index - i) * LEFT * 2))

                rect_list[i], rect_list[min_index] = rect_list[min_index], rect_list[i]

            sorted_rect_list.append(rect_list[i])
            if sorted_brace:
                self.remove(sorted_brace)

            sorted_brace = BraceText(VGroup(*sorted_rect_list), SORTED_TEXT)
            self.add(sorted_brace)

        self.wait(1)
        sorted_rect_list.append(rect_list[len(rect_list) - 1])
        if sorted_brace:
            self.remove(sorted_brace)
        sorted_brace = BraceText(VGroup(*sorted_rect_list), SORTED_TEXT)
        self.add(sorted_brace)

        self.wait()
