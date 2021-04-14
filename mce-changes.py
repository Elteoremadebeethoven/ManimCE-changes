from manim import *

"""
 _     _   _          ____ ___  _   _ _____ ___ ____       _ _      _
/ |   | \ | | ___    / ___/ _ \| \ | |  ___|_ _/ ___|   __| (_) ___| |_
| |   |  \| |/ _ \  | |  | | | |  \| | |_   | | |  _   / _` | |/ __| __|
| |_  | |\  | (_) | | |__| |_| | |\  |  _|  | | |_| | | (_| | | (__| |_
|_(_) |_| \_|\___/   \____\___/|_| \_|_|   |___\____|  \__,_|_|\___|\__|
"""

class NewGraphScene(GraphScene):
    def __init__(self):
        super().__init__(
            graph_origin=[-6,-3,0],
            x_axis_width=13,
            y_axis_height=7,
            x_max=13,
            x_axis_label="$t$",
            y_axis_label="$d$"
        )

    def setup(self):
        GraphScene.setup(self)
        self.setup_parabola_config()
        self.setup_graph_parabola()
        self.setup_area_config()

    def setup_parabola_config(self):
        h, k = 4, 9

        self.parabola_func = lambda x: - (x - h) ** 2 + k
        self.inverse_parabola_func = lambda x, s: 4 + s * np.sqrt(k - x)
        self.d_parabola = lambda x: (2 * h) - 2 * x
        self.max_parabola = h


    def setup_graph_parabola(self):
        self.parabola_config = {
            "func": self.parabola_func,
            "x_min": self.inverse_parabola_func(-1,-1),
            "x_max": self.inverse_parabola_func(-1,1),
            "color": GREEN,
        }

    def setup_area_config(self):
        self.area_config = {
            "t_min": self.max_parabola,
            "t_max": self.inverse_parabola_func(0,1),
            "dx_scaling": 0.1,
        }


    def construct(self):
        self.setup_axes(animate=False)
        parabola = self.get_graph(**self.parabola_config)

        del self.parabola_config["func"]
        # get_derivative_graph is not perfect
        d_parabola = self.get_derivative_graph(parabola,**self.parabola_config)
        d_parabola = DashedVMobject(d_parabola, num_dashes=40)

        parabola_area = self.get_area(parabola,**self.area_config)
        parabola_area.set_color_by_gradient(RED,PURPLE)
        parabola_area.set_fill(opacity=0.9)

        secant_group = self.get_secant_slope_group(5,parabola,dx=1)

        dot = Dot()
        # move dot at graph(x=6)
        dot.move_to(self.input_to_graph_point(6,parabola))
        v_line_at_6 = self.get_vertical_line_to_graph(6,parabola)
        h_line_at_6 = Line(dot.get_center(),[self.graph_origin[0],dot.get_y(),0])

        VGroup(v_line_at_6,h_line_at_6).set_color(ORANGE)

        self.add(
            parabola,
            d_parabola,
            parabola_area,
            secant_group,
            v_line_at_6,
            h_line_at_6,
            dot,
        )

        self.animate_secant_slope_group_change(secant_group,target_dx=0.1)
        self.wait()

"""
 ____                   _                 _                        _   _               _
|___ \       __ _ _ __ (_)_ __ ___   __ _| |_ ___   _ __ ___   ___| |_| |__   ___   __| |
  __) |     / _` | '_ \| | '_ ` _ \ / _` | __/ _ \ | '_ ` _ \ / _ \ __| '_ \ / _ \ / _` |
 / __/ _   | (_| | | | | | | | | | | (_| | ||  __/ | | | | | |  __/ |_| | | | (_) | (_| |
|_____(_) (_)__,_|_| |_|_|_| |_| |_|\__,_|\__\___| |_| |_| |_|\___|\__|_| |_|\___/ \__,_|
"""

class AnimateMethod(Scene):
    def construct(self):
        sq = Square()
        sq.save_state()
        self.add(sq)

        # New form
        self.play(
            sq.animate.to_edge(DOWN,buff=1)
        )
        self.wait()

        self.play(Restore(sq))
        self.wait()

        # Multiple methods
        self.play(
            sq.animate
                .scale(2)
                .set_color(ORANGE)
                .to_corner(UR,buff=1)
        )
        self.wait()


# If you need it as a class Animation

class AnimateMethod2(Scene):
    def construct(self):
        sq = Square()
        sq.save_state()
        self.add(sq)

        # New form
        self.play(
            ApplyMethod(sq.to_edge,UP,{"buff":1.5})
        )
        self.wait()

        self.play(Restore(sq))
        self.wait()

        # Multiple methods
        self.play(
            ApplyFunction(
                lambda mob: mob.scale(2)\
                               .set_color(ORANGE)\
                               .to_corner(UR,buff=1),
                sq
            )
        )
        self.wait()

"""
 _____    ____             _                                   _
|___ /   | __ )  __ _  ___| | ____ _ _ __ ___  _   _ _ __   __| |
  |_ \   |  _ \ / _` |/ __| |/ / _` | '__/ _ \| | | | '_ \ / _` |
 ___) |  | |_) | (_| | (__|   < (_| | | | (_) | |_| | | | | (_| |
|____(_) |____/ \__,_|\___|_|\_\__, |_|  \___/ \__,_|_| |_|\__,_|
                               |___/
                 _    __
  __ _ _ __   __| |  / _|_ __  ___
 / _` | '_ \ / _` | | |_| '_ \/ __|
| (_| | | | | (_| | |  _| |_) \__ \
 \__,_|_| |_|\__,_| |_| | .__/|___/
                        |_|
"""

# If you define properties in the code then 
# the parser (commands per terminal) will be ignored.

# config["frame_rate"] = 29
# config["pixel_width"] = 800
# config["pixel_height"] = 800

class ChangeProperties(Scene):
    def construct(self):
        # Change color
        self.camera.background_color = RED
        sq = Square()
        sq.add_updater(lambda mob,dt: mob.rotate(20*DEGREES*dt))

        fps = self.camera.frame_rate
        FRAME_HEIGHT = self.camera.frame_height
        FRAME_WIDTH = self.camera.frame_width

        logger.info(f"fps: {fps}")
        logger.info(f"width: {FRAME_WIDTH}")
        logger.info(f"height: {FRAME_HEIGHT}")
        logger.info(f"ratio: {FRAME_WIDTH / FRAME_HEIGHT}")
        print("\n")

        self.add(sq)
        self.wait(2)
        self.camera.background_color = ORANGE
        self.wait(3)


# If it is defined twice, the one that is lower will be taken.
# config["frame_rate"] = 30


class ChangeBC(Scene):
    def change_background_color(self,color_target):
        base_color = self.camera.background_color
        def update_bc(mob,alpha):
            self.camera.background_color = \
                interpolate_color(base_color, color_target, alpha)
        return UpdateFromAlphaFunc(Mobject(),update_bc)

    def construct(self):
        self.camera.background_color = PINK
        target_color = TEAL

        self.play(self.change_background_color(target_color))
        self.wait()


"""
 _  _      _____            ___     _____         _
| || |    |_   _|____  __  ( _ )   |_   _|____  _| |_
| || |_     | |/ _ \ \/ /  / _ \/\   | |/ _ \ \/ / __|
|__   _|    | |  __/>  <  | (_>  <   | |  __/>  <| |_
   |_|(_)   |_|\___/_/\_\  \___/\/   |_|\___/_/\_\\__|
"""

paragraph_string = \
"""This is a simple
paragraph multi-line
"""

class TexAndText(Scene):
    def construct(self):
        tex = Tex("Hi, this is \\LaTeX")
        formula = MathTex("e^{i\\pi}+1=0")
        text = Text("This is a simple text",font="Arial")
        paragraph = Paragraph(paragraph_string).scale(0.7)

        grp = VGroup(tex,formula,text,paragraph)
        grp.arrange(DOWN)
        # don't use set_width or set_height
        grp.set(width=config["frame_width"]-1)

        self.add(grp)


