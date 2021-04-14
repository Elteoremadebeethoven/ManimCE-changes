from manim import *

"""
 __  __            _              _____         _
|  \/  | __ _ _ __| | ___   _ _ _|_   _|____  _| |_
| |\/| |/ _` | '__| |/ / | | | '_ \| |/ _ \ \/ / __|
| |  | | (_| | |  |   <| |_| | |_) | |  __/>  <| |_
|_|  |_|\__,_|_|  |_|\_\\__,_| .__/|_|\___/_/\_\\__|
                             |_|
"""

# DOCS:
# https://docs.manim.community/en/stable/reference/manim.mobject.svg.text_mobject.MarkupText.html?highlight=markup#manim.mobject.svg.text_mobject.MarkupText

class BasicMarkupExample(Scene):
    def construct(self):
        text1 = MarkupText("<b>foo</b> <i>bar</i> <b><i>foobar</i></b>")
        text2 = MarkupText("<s>foo</s> <u>bar</u> <big>big</big> <small>small</small>")
        text3 = MarkupText("H<sub>2</sub>O and H<sub>3</sub>O<sup>+</sup>")
        text4 = MarkupText("type <tt>help</tt> for help")
        text5 = MarkupText(
            '<span underline="double">foo</span> <span underline="error">bar</span>'
        )
        group = VGroup(text1, text2, text3, text4, text5).arrange(DOWN)
        group.scale(1.4)
        self.add(group)

"""
  ____          _      __  __       _     _           _
 / ___|___   __| | ___|  \/  | ___ | |__ (_) ___  ___| |_
| |   / _ \ / _` |/ _ \ |\/| |/ _ \| '_ \| |/ _ \/ __| __|
| |__| (_) | (_| |  __/ |  | | (_) | |_) | |  __/ (__| |_
 \____\___/ \__,_|\___|_|  |_|\___/|_.__// |\___|\___|\__|
                                       |__/
"""

# DOCS:
# https://docs.manim.community/en/stable/reference/manim.mobject.svg.code_mobject.Code.html?highlight=code#manim.mobject.svg.code_mobject.Code

PYTHON_CODE = \
'''from manim import Scene, Square, Create

class FadeInSquare(Scene):
    def construct(self):
        s = Square()
        self.play(Create(s))
        self.play(s.animate.scale(2))
        self.wait()
'''

class CodeFromString(Scene):
    def construct(self):
        code_kwargs = {
            "code": PYTHON_CODE,
            "tab_width": 4,
            "background": "window",
            "language": "Python",
            "font": "Monospace",
            "style": "monokai"
        }
        code = Code(**code_kwargs)
        code.move_to(ORIGIN)
        self.draw_code_all_lines_at_a_time(code,run_time=3)
        self.wait()
        self.play(code.animate.to_edge(UP).scale(0.8))
        self.wait()

        FRAME_SCALE = 0.45
        frame = Rectangle(
            width=config["frame_width"],
            height=config["frame_height"],
        )
        frame.scale(FRAME_SCALE)
        frame.next_to(code,DOWN)

        # ShowCreation -> Create
        line = self.get_remark_rectangle(code, 1)
        # from manim import Scene, Square
        line.save_state()
        line.stretch(0.01,0) # set_width(0.01,0) 0 is x direction
        # line.set_fill(opacity=0)
        self.add(line)
        self.play(Restore(line))
        self.wait()
        self.play(Create(frame))
        # class FadeInSquare(Scene):
        self.change_line(code, line, 3)
        # def construct(self)
        self.change_line(code, line, 4)
        # s = Square()
        self.change_line(code, line, 5)
        # self.play(Create(s))
        self.change_line(code, line, 6)
        square = Square()
        square.scale(FRAME_SCALE)
        square.move_to(frame)
        self.play(Create(square))
        # self.play(s.animate.scale(2))
        self.change_line(code, line, 7)
        self.play(square.animate.scale(2))
        # self.wait()
        self.change_line(code, line, 8)
        self.wait()

    def draw_code_all_lines_at_a_time(self, code, **kwargs):
        self.play(LaggedStart(*[
                Write(code[i]) 
                for i in range(code.__len__())
            ]),
            **kwargs
        )

    def get_remark_rectangle(
            self, 
            code, 
            line, 
            fill_opacity=0.4, 
            stroke_width=0,
            fill_color=YELLOW,
            **kwargs):
        lines = VGroup(code[2],code[1])
        w, h = getattr(lines, "width"), getattr(lines, "height")
        frame = Rectangle(width=w,height=h)

        code_line = code[1][line-1]
        line_rectangle = Rectangle(
            width=w,
            height=getattr(code[1][line-1],"height")*1.5,
            fill_opacity=fill_opacity,
            stroke_width=stroke_width,
            fill_color=fill_color,
            **kwargs
        )
        line_rectangle.set_y(code_line.get_y())
        line_rectangle.scale([1.1,1,1])
        return line_rectangle

    def change_line(self, code, rect, next_line, *args, **kwargs):
        self.play(
            Transform(
                rect,
                self.get_remark_rectangle(code, next_line),
            ),
            *args,
            **kwargs,
        )

"""
    _
   / \   _ __ _ __ _____      _____
  / _ \ | '__| '__/ _ \ \ /\ / / __|
 / ___ \| |  | | | (_) \ V  V /\__ \
/_/   \_\_|  |_|  \___/ \_/\_/ |___/
"""

# DOCS
# https://docs.manim.community/en/stable/reference/manim.mobject.geometry.Arrow.html?highlight=arrows

# You need to import them:
from manim.mobject.geometry import (
    ArrowCircleFilledTip,
    ArrowCircleTip,
    ArrowSquareFilledTip,
    ArrowSquareTip,
    ArrowTriangleFilledTip,
    ArrowTriangleTip
)

class NewArrows(Scene):
    def construct(self):
        tips_set = [
            ArrowCircleFilledTip,
            ArrowCircleTip,
            ArrowSquareFilledTip,
            ArrowSquareTip,
            ArrowTriangleFilledTip,
            ArrowTriangleTip
        ]
        normal_arrow = VGroup(*[
            Arrow(LEFT*2,RIGHT*2, tip_shape=ts)
            for ts in tips_set
        ]).arrange(DOWN,buff=0.4)

        double_arrow = VGroup(*[
            DoubleArrow(LEFT*2,RIGHT*2, tip_shape_start=ts, tip_shape_end=ts)
            for ts in tips_set
        ]).arrange(DOWN,buff=0.4)

        normal_arrow_t = Text("Arrow",font="Monospace")
        double_arrow_t = Text("DoubleArrow",font="Monospace")

        VGroup(
            VGroup(normal_arrow_t,normal_arrow).arrange(DOWN),
            VGroup(double_arrow_t,double_arrow).arrange(DOWN),
        ).arrange(RIGHT,buff=1)

        self.play(
            Write(normal_arrow_t),
            Write(double_arrow_t),
            LaggedStartMap(
                GrowArrow,normal_arrow
            ),
            LaggedStartMap(
                GrowArrow,double_arrow
            ),
            run_time=4
        )
        self.wait(3)

"""
 _   _
| \ | | _____      __
|  \| |/ _ \ \ /\ / /
| |\  |  __/\ V  V /
|_| \_|\___| \_/\_/

 _____                     __                            _   _
|_   _| __ __ _ _ __  ___ / _| ___  _ __ _ __ ___   __ _| |_(_) ___  _ __  ___
  | || '__/ _` | '_ \/ __| |_ / _ \| '__| '_ ` _ \ / _` | __| |/ _ \| '_ \/ __|
  | || | | (_| | | | \__ \  _| (_) | |  | | | | | | (_| | |_| | (_) | | | \__ \
  |_||_|  \__,_|_| |_|___/_|  \___/|_|  |_| |_| |_|\__,_|\__|_|\___/|_| |_|___/
"""

# DOCS
# https://docs.manim.community/en/stable/reference/manim.animation.transform_matching_parts.TransformMatchingTex.html#manim.animation.transform_matching_parts.TransformMatchingTex

class IsolateTex1(Scene):
    def construct(self):
        t1 = MathTex("{{x}}")
        t2 = MathTex("{{x}} - {{x}}")
        VGroup(t1,t2)\
            .scale(3)\
            .arrange(DOWN)

        self.add(t1)
        self.wait()
        self.play(
            TransformMatchingTex(t1,t2),
            run_time=4
        )
        self.wait()


class IsolateTex1v2(Scene):
    def construct(self):
        isolate_tex = ["x"]
        t1 = MathTex("x",substrings_to_isolate=isolate_tex)
        t2 = MathTex("x - x",substrings_to_isolate=isolate_tex)
        VGroup(t1,t2)\
            .scale(3)\
            .arrange(DOWN)

        self.add(t1)
        self.wait()
        self.play(
            TransformMatchingTex(t1,t2),
            run_time=4
        )
        self.wait()


class IsolateTex1v3(Scene):
    def construct(self):
        t1 = MathTex("x")
        t2 = MathTex("x - x")
        VGroup(t1,t2)\
            .scale(3)\
            .arrange(DOWN)

        self.add(t1)
        self.wait()
        self.play(
            # If the formula is complex this animation will not work.
            TransformMatchingShapes(t1,t2),
            run_time=4
        )
        self.wait()


class IsolateTex2(Scene):
    def construct(self):
        isolate_tex = ["x","y","3","="]
        t1 = MathTex("x+y=3",substrings_to_isolate=isolate_tex)
        t2 = MathTex("x=3-y",substrings_to_isolate=isolate_tex)
        VGroup(t1,t2)\
            .scale(3)
        t2.align_to(t1,LEFT)

        self.add(t1)
        self.wait()
        self.play(
            TransformMatchingTex(
                t1,t2,
                # Try removing this dictionary
                key_map={
                    "+":"-"
                }
            ),
            run_time=4
        )
        self.wait()

class IsolateTex3(Scene):
    def construct(self):
        isolate_tex = ["a","b","c","="]
        t1 = MathTex("a \\times b = c",substrings_to_isolate=isolate_tex)
        t2 = MathTex("a = { c \\over b }",substrings_to_isolate=isolate_tex)
        VGroup(t1,t2)\
            .scale(3)
        t2.align_to(t1,LEFT)

        self.add(t1)
        self.wait()
        self.play(
            TransformMatchingTex(
                t1,t2,
                key_map={
                    "\\times":"\\over"
                }
            ),
            run_time=4
        )
        self.wait()


#  _____         _     _____                     __
# |  ___|_ _  __| | __|_   _| __ __ _ _ __  ___ / _| ___  _ __ _ __ ___  
# | |_ / _` |/ _` |/ _ \| || '__/ _` | '_ \/ __| |_ / _ \| '__| '_ ` _ \ 
# |  _| (_| | (_| |  __/| || | | (_| | | | \__ \  _| (_) | |  | | | | | |
# |_|  \__,_|\__,_|\___||_||_|  \__,_|_| |_|___/_|  \___/|_|  |_| |_| |_|


class FadeTransformExample(Scene):
    def construct(self):
        m1 = Text("Hello world").to_corner(UL)
        m2 = Text("I'm FadeTransform").to_corner(DR)

        self.add(m1)
        self.wait()
        self.play(
            # Equivalent to ReplacementTransform
            FadeTransform(m1,m2),
            run_time=4
        )


class StrangeTransformFail(Scene):
    def construct(self):
        t1 = MathTex("e^","\\frac{-it\\pi}{\\omega}")
        t2 = MathTex("\\frac{-it\\pi}{\\omega}")
        VGroup(t1,t2)\
            .scale(3)\
            .arrange(DOWN,buff=2)
            
        self.add(t1,t2.copy().fade(0.8))
        self.wait()
        self.play(
            TransformFromCopy(t1[-1],t2[0]),
            run_time=6
        )
        self.wait()

class StrangeTransform(Scene):
    def construct(self):
        t1 = MathTex("e^","\\frac{-it\\pi}{\\omega}")
        t2 = MathTex("\\frac{-it\\pi}{\\omega}")
        VGroup(t1,t2)\
            .scale(3)\
            .arrange(DOWN,buff=2)
            
        self.add(t1,t2.copy().fade(0.8))
        self.wait()
        self.play(
            FadeTransformPieces(t1[-1].copy(),t2[0]),
            run_time=4
        )
        self.wait()

"""
  ____          _
 / ___|   _ ___| |_ ___  _ __ ___
| |  | | | / __| __/ _ \| '_ ` _ \
| |__| |_| \__ \ || (_) | | | | | |
 \____\__,_|___/\__\___/|_| |_| |_|

 _               _                       _       _
| |_ _____  __  | |_ ___ _ __ ___  _ __ | | __ _| |_ ___  ___
| __/ _ \ \/ /  | __/ _ \ '_ ` _ \| '_ \| |/ _` | __/ _ \/ __|
| ||  __/>  <   | ||  __/ | | | | | |_) | | (_| | ||  __/\__ \
 \__\___/_/\_\___\__\___|_| |_| |_| .__/|_|\__,_|\__\___||___/
            |_____|               |_|
"""

# Example from example_scenes/advanced_tex_fonts.py

TemplateForFrenchCursive = TexTemplate(
    preamble=r"""
\usepackage[english]{babel}
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage[T1]{fontenc}
\usepackage[default]{frcursive}
\usepackage[eulergreek,noplusnominus,noequal,nohbar,%
nolessnomore,noasterisk]{mathastext}
"""
)


def FrenchCursive(*tex_strings, **kwargs):
    return Tex(*tex_strings, tex_template=TemplateForFrenchCursive, **kwargs)


class TexFontTemplateManual(Scene):
    """An example scene that uses a manually defined TexTemplate() object to create
    LaTeX output in French Cursive font"""

    def construct(self):
        self.add(Tex("Tex Font Example").to_edge(UL))
        self.play(Write(FrenchCursive("$f: A \\longrightarrow B$").shift(UP)))
        self.play(Write(FrenchCursive("Behold! We can write math in French Cursive")))
        self.wait(1)
        self.play(
            Write(
                Tex(
                    "See more font templates at \\\\ http://jf.burnol.free.fr/showcase.html"
                ).shift(2 * DOWN)
            )
        )
        self.wait(2)

#  __  __           _     _____   __  __
# |  \/  |_   _ ___(_) __|_   _|__\ \/ /
# | |\/| | | | / __| |/ __|| |/ _ \\  /
# | |  | | |_| \__ \ | (__ | |  __//  \
# |_|  |_|\__,_|___/_|\___||_|\___/_/\_\

TemplateForMusicTeX = TexTemplate(
    preamble=r"""
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage{mtxlatex}
\usepackage{graphicx}
"""
)

def MusicTeX(*tex_strings, **kwargs):
    return Tex(
        *tex_strings,
        tex_template=TemplateForMusicTeX,
        tex_environment="music", # <- Change enviroment
        **kwargs
    )

class MusicTeXExample(Scene):
    def construct(self):
        template = MusicTeX(r"""
            \parindent10mm
            \instrumentnumber{1}
            \setname1{Piano}
            \setstaffs1{2} 
            \generalmeter{\meterfrac44}
            \startextract 
            \Notes\ibu0f0\qb0{cge}\tbu0\qb0g|\hl j\en
            \Notes\ibu0f0\qb0{cge}\tbu0\qb0g|\ql l\sk\ql n\en
            \bar
            \Notes\ibu0f0\qb0{dgf}|\qlp i\en
            \notes\tbu0\qb0g|\ibbl1j3\qb1j\tbl1\qb1k\en
            \Notes\ibu0f0\qb0{cge}\tbu0\qb0g|\hl j\en
            \zendextract
        """)
        template.set(width=config["frame_width"]-1)
        self.play(
            Write(template)
        )
        self.wait(2)

#  ______     ______            _ _   _                 _
# / ___\ \   / / ___| __      _(_) |_| |__     ___ ___ | | ___  _ __ ___
# \___ \\ \ / / |  _  \ \ /\ / / | __| '_ \   / __/ _ \| |/ _ \| '__/ __|
#  ___) |\ V /| |_| |  \ V  V /| | |_| | | | | (_| (_) | | (_) | |  \__ \
# |____/  \_/  \____|   \_/\_/ |_|\__|_| |_|  \___\___/|_|\___/|_|  |___/

# svg: https://www.flaticon.com/free-icon/notification_4457183?related_id=4457183&origin=pack

class SVGColor(Scene):
    def construct(self):
        logger.warning("If the SVG is not well built then it will not work.")
        svg = SVGMobject("./assets/svg_images/notification")
        svg.set(height=config["frame_height"]-1)
        self.play(
            LaggedStartMap(
                DrawBorderThenFill,svg
            )
        )
        self.wait()
        self.play(
            LaggedStartMap(
                FadeIn,svg
            )
        )
        self.wait()


"""
 _____                           _              __
| ____|_  ____ _ _ __ ___  _ __ | | ___  ___   / _|_ __ ___  _ __ ___
|  _| \ \/ / _` | '_ ` _ \| '_ \| |/ _ \/ __| | |_| '__/ _ \| '_ ` _ \
| |___ >  < (_| | | | | | | |_) | |  __/\__ \ |  _| | | (_) | | | | | |
|_____/_/\_\__,_|_| |_| |_| .__/|_|\___||___/ |_| |_|  \___/|_| |_| |_|
                          |_|
 _____          _ _   _
|_   _|_      _(_) |_| |_ ___ _ __
  | | \ \ /\ / / | __| __/ _ \ '__|
  | |  \ V  V /| | |_| ||  __/ |
  |_|   \_/\_/ |_|\__|\__\___|_|
"""

# from: https://github.com/ManimCommunity/manim-tweets

class IntroBanner(Scene):
    def construct(self):
        self.camera.background_color = "#ece6e2"
        banner_location = ORIGIN

        banner = ManimBanner(dark_theme=False).scale(0.9).move_to(banner_location)
        banner.scale_factor = 2.5
        self.play(banner.create())

        for mob in [banner.triangle, banner.circle, banner.square]:
            mob.clear_updaters()
        self.bring_to_front(banner.M)

        # Position the targets of the M.
        bw = getattr(banner.anim,"width")
        banner.M.generate_target().shift(LEFT * bw * 0.57),

        # Position the anim based on the location of the target.
        banner.anim.next_to(banner.M.target, RIGHT, 0.1)
        banner.anim.align_to(banner.M.target, DOWN)

        self.play(
            banner.M.animate.shift(LEFT * bw * 0.57),
            banner.triangle.animate.shift(RIGHT * bw * 0.57),
            banner.square.animate.shift(RIGHT * bw * 0.57),
            banner.circle.animate.shift(RIGHT * bw * 0.57),
            LaggedStart(*[
                FadeIn(mob)
                for mob in banner.anim
                ],
                lag_ratio=0.1,
                run_time=1.7
            )
        )

        self.wait()

#---------------------------

class HamiltonianCycle(Scene):
    def construct(self):
        dots = [Dot(z_index=30) for _ in range(20)]
        for ind, dot in enumerate(dots[:5]):
            dot.move_to(
                3.75
                * (
                    np.cos(ind / 5 * TAU + TAU / 4) * RIGHT
                    + np.sin(ind / 5 * TAU + TAU / 4) * UP
                )
            )
        for ind, dot in enumerate(dots[5:10]):
            dot.move_to(
                2.75
                * (
                    np.cos(ind / 5 * TAU + TAU / 4) * RIGHT
                    + np.sin(ind / 5 * TAU + TAU / 4) * UP
                )
            )
        for ind, dot in enumerate(dots[10:15]):
            dot.move_to(
                1.5
                * (
                    np.cos(ind / 5 * TAU - TAU / 4) * RIGHT
                    + np.sin(ind / 5 * TAU - TAU / 4) * UP
                )
            )
        for ind, dot in enumerate(dots[15:]):
            dot.move_to(
                0.75
                * (
                    np.cos(ind / 5 * TAU - TAU / 4) * RIGHT
                    + np.sin(ind / 5 * TAU - TAU / 4) * UP
                )
            )
        lines = (
            [
                Line(dots[k].get_center(), dots[(k + 1) % 5].get_center())
                for k in range(5)
            ]
            + [Line(dots[k].get_center(), dots[5 + k].get_center()) for k in range(5)]
            + [
                Line(dots[5 + k].get_center(), dots[10 + (k + 2) % 5].get_center())
                for k in range(5)
            ]
            + [
                Line(dots[5 + k].get_center(), dots[10 + (k + 3) % 5].get_center())
                for k in range(5)
            ]
            + [
                Line(dots[10 + k].get_center(), dots[15 + k].get_center())
                for k in range(5)
            ]
            + [
                Line(dots[15 + k].get_center(), dots[15 + (k + 1) % 5].get_center())
                for k in range(5)
            ]
        )
        vgroup = VGroup(*lines, *dots)
        vgroup.move_to(ORIGIN)
        self.play(*[Create(dot) for dot in dots])
        self.play(*[Create(line) for line in lines])
        self.wait(1)
        cycle_ind = [
            0,
            1,
            2,
            7,
            14,
            6,
            13,
            5,
            12,
            9,
            11,
            16,
            17,
            18,
            19,
            15,
            10,
            8,
            3,
            4,
        ]
        cycle_lines = []
        for k in range(len(cycle_ind)):
            self.play(
                dots[cycle_ind[k]].animate.set_color(RED), run_time=0.3, rate_function=linear
            )
            new_line = Line(
                dots[cycle_ind[k]].get_center(),
                dots[cycle_ind[(k + 1) % len(cycle_ind)]].get_center(),
                color=RED,
                stroke_width=5,
            )
            cycle_lines.append(new_line)
            self.play(Create(new_line), run_time=0.65)
        self.wait(1)
        self.play(VGroup(vgroup, *cycle_lines).animate.shift(3 * LEFT))
        t1 = Tex("The graph")
        t1.next_to(vgroup, RIGHT)
        self.play(Write(t1))
        self.play(
            ApplyFunction(
                lambda obj: obj.scale(0.2).next_to(t1, RIGHT).shift(0.4 * UP),
                VGroup(*lines, *dots).copy(),
            )
        )
        t2 = Tex("has a Hamiltonian cycle.")
        t2.next_to(t1, DOWN)
        t2.align_to(t1, LEFT)
        self.play(Write(t2))
        self.wait()
        self.play(*[FadeOut(obj) for obj in self.mobjects])

# --------------------------

class Lissajous(Scene):
    def construct(self):
        # Simultaneous lissajous curves.
        lissajous_size = 2
        lissajous_a = 1
        lissajous_b = 1
        lissajous_alpha = ValueTracker()
        offset = PI / 2

        def lissajous_location(t, delta):
            A = lissajous_size
            a = lissajous_a
            b = lissajous_b
            x = A * np.sin(a * t + offset)
            y = A * np.sin(b * t + delta + offset)
            return x * RIGHT + y * UP

        def get_line_length(mob):
            length = 0
            start_anchors = mob.get_start_anchors()
            for i in range(len(start_anchors) - 1):
                length += get_norm(start_anchors[i + 1] - start_anchors[i])
            return length

        def grow_line(mob):
            new_position = lissajous_location(
                lissajous_alpha.get_value() * mob.rate, mob.delta
            )

            # Update line length.
            mob.add_line_to(new_position)
            mob.line_length += get_norm(new_position - mob.points[-1])

            while get_line_length(mob) > mob.maximum_length:
                mob.set_points(mob.points[4:])

        def get_lissajous_line(delta, rate):
            line = VMobject()
            line.delta = delta
            line.line_length = 0
            line.maximum_length = 8
            line.rate = rate
            line.points = np.array([lissajous_location(0, line.delta)])
            line.add_updater(grow_line)
            return line

        for i,color in enumerate([RED,ORANGE,YELLOW,GREEN,BLUE,BLUE_B,PURPLE]):
            self.add(get_lissajous_line((i+1) * PI / 8, i+1).set_color(color))

        self.play(lissajous_alpha.animate.set_value(20), run_time=32, rate_func=linear)


# ------------------------------------------------

import random
import math


class BinarySearchTree(VGroup):
    def __init__(
        self,
        scene,
        levels=3,
        base_offset=0.5,
        node_radius=0.5,
        child_offset_factor=1.2,
        label_scale_factor=1,
        color_nodes=False,
        max_value=16,
        animation_runtime=0.2,
        insertion_initial_offset=1,
    ):
        super().__init__()
        self.scene = scene
        self.empty = True
        self.child_down_offset = DOWN * child_offset_factor
        self.child_left_offset = LEFT * base_offset * 2 * math.log2(levels)
        self.node_radius = node_radius
        self.label_scale_factor = label_scale_factor
        self.color_nodes = color_nodes
        self.max_value = max_value
        self.animation_runtime = animation_runtime
        self.insertion_initial_offset = insertion_initial_offset

        self.root = self.get_node(None)
        self.add(self.root)

    def get_node(self, value):
        node = VDict(
            {
                "node": Circle(radius=self.node_radius, color=WHITE),
                "label": MathTex("\\varnothing" if value is None else str(value)).scale(
                    self.label_scale_factor
                ),
            }
        )
        if self.label_scale_factor != 0:
            node["label"] = MathTex(
                "\\varnothing" if value is None else str(value)
            ).scale(self.label_scale_factor)
        if value is not None:
            node_color = interpolate_color(BLUE, RED, value / self.max_value)
            node.set_stroke(node_color)
            if self.color_nodes:
                node.set_fill(node_color, opacity=1)
            node.color = node_color
        node.value = value
        node.left_child = None
        node.right_child = None
        return node

    def insert(self, value):
        node = self.get_node(value)
        if self.root.value is None:
            node.move_to(self.root.get_center())
            self.scene.play(
                FadeInFrom(node, UP * self.insertion_initial_offset),
                FadeOut(self.root),
                run_time=self.animation_runtime,
            )
            self.remove(self.root)
            self.root = node
            self.add(node)
            self.empty = False
            return

        node.move_to(self.root.get_center() + UP * self.insertion_initial_offset)
        cur_node = self.root
        child_left_offset = self.child_left_offset.copy()
        while cur_node is not None:
            if node.value <= cur_node.value:
                self.scene.play(
                    node.animate.move_to(cur_node.get_center() + 2 * cur_node["node"].radius * LEFT),
                    run_time=self.animation_runtime,
                )
                if cur_node.left_child is not None:
                    cur_node = cur_node.left_child
                else:
                    child_location = (
                        cur_node.get_center()
                        + self.child_down_offset
                        + child_left_offset
                    )
                    parent_child_vector = normalize(
                        child_location - cur_node.get_center()
                    )

                    edge_start = (
                        cur_node.get_center() + parent_child_vector * self.node_radius
                    )
                    edge_end = child_location - parent_child_vector * self.node_radius
                    edge = Line(edge_start, edge_end, stroke_color=node.color)

                    self.scene.play(
                        node.animate.move_to(child_location),
                        FadeIn(edge),
                        run_time=self.animation_runtime,
                    )
                    cur_node.left_child = node
                    self.add(node, edge)
                    break
            else:
                self.scene.play(
                    node.animate.move_to(cur_node.get_center() + 2 * cur_node["node"].radius * RIGHT),
                    run_time=self.animation_runtime,
                )
                if cur_node.right_child is not None:
                    cur_node = cur_node.right_child
                else:
                    child_location = (
                        cur_node.get_center()
                        + self.child_down_offset
                        - child_left_offset
                    )
                    parent_child_vector = normalize(
                        child_location - cur_node.get_center()
                    )

                    edge_start = (
                        cur_node.get_center() + parent_child_vector * self.node_radius
                    )
                    edge_end = child_location - parent_child_vector * self.node_radius
                    edge = Line(edge_start, edge_end, stroke_color=node.color)

                    self.scene.play(
                        node.animate.move_to(child_location),
                        FadeIn(edge),
                        run_time=self.animation_runtime,
                    )
                    cur_node.right_child = node
                    self.add(node, edge)
                    break
            child_left_offset /= 2


class BinarySearchTreeAnimation(Scene):
    def construct(self):
        tree = BinarySearchTree(self, base_offset=0.75, max_value=16).shift(UP * 2)
        self.add(tree)
        label = (
            Text("Great for storing structured data.").scale(0.8).to_edge(UP, buff=0.1)
        )
        self.add(label)

        nums = [8, 4, 2, 1, 3, 6, 5, 7, 12, 10, 9, 11, 14, 13, 15]
        for i in nums:
            tree.insert(i)

        self.wait(0.5)
        self.play(FadeOut(tree))
        self.remove(label)


# -----------------------------------

class MmodNTrackerFigure(Scene):
    # I make my own rules
    CONFIG = {
        "number_of_lines": 20,
        "gradient_colors":[RED,YELLOW,BLUE],
        "start_value": 0,
        "end_value": 10,
        "total_time":10,
        "figure": Triangle()
    }
    def construct(self):
        figure = self.CONFIG["figure"]
        figure.set(height=config["frame_height"]-1)
        mod_tracker = ValueTracker(self.CONFIG["start_value"])
        lines = self.get_m_mod_n_objects(figure,mod_tracker.get_value())
        lines.add_updater(
            lambda mob: mob.become(
                self.get_m_mod_n_objects(figure,mod_tracker.get_value())
                )
            )
        self.add(figure,lines)
        self.wait()
        self.play(
            mod_tracker.animate.set_value(self.CONFIG["end_value"]),
            rate_func=linear,
            run_time=self.CONFIG["total_time"]
            )
        self.wait()

    def get_m_mod_n_objects(self,figure,x,y=None):
        if y==None:
            y = self.CONFIG["number_of_lines"]
        lines = VGroup()
        for i in range(y):
            start_point = figure.point_from_proportion((i%y)/y)
            end_point = figure.point_from_proportion(((i*x)%y)/y)
            line = Line(start_point,end_point).set_stroke(width=1)
            lines.add(line)
        lines.set_color_by_gradient(*self.CONFIG["gradient_colors"])
        return lines


def regular_vertices(n, *, radius=1, start_angle=None):
    if start_angle is None:
        if n % 2 == 0:
            start_angle = 0
        else:
            start_angle = TAU / 4

    start_vector = rotate_vector(RIGHT * radius, start_angle)
    vertices     = compass_directions(n, start_vector)

    return vertices, start_angle

class Star(Polygon):
    def __init__(self, n=6, *, density=2, outer_radius=1, inner_radius=None, start_angle=None, **kwargs):
        if density <= 0 or density >= n / 2:
            raise ValueError(f"Incompatible density {density}")

        inner_angle = TAU / (2 * n)

        if inner_radius is None:
            # Calculate the inner radius for n and density.
            # See https://math.stackexchange.com/a/2136292

            outer_angle = TAU * density / n

            inverse_x = 1 - np.tan(inner_angle) * ((np.cos(outer_angle) - 1) / np.sin(outer_angle))

            inner_radius = outer_radius / (np.cos(inner_angle) * inverse_x)

        outer_vertices, self.start_angle = regular_vertices(n, radius=outer_radius, start_angle=start_angle)
        inner_vertices, _                = regular_vertices(n, radius=inner_radius, start_angle=self.start_angle + inner_angle)

        vertices = []
        for pair in zip(outer_vertices, inner_vertices):
            vertices.extend(pair)

        super().__init__(*vertices, **kwargs)


class MmodNTrackerStar(MmodNTrackerFigure):
    # I make my own rules
    CONFIG = {
        "number_of_lines": 300,
        "gradient_colors":[RED,YELLOW,BLUE],
        "start_value": 1,
        "end_value": 2,
        "total_time": 5,
        "figure": Star()
    }