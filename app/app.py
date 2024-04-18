import seaborn as sns
from faicons import icon_svg

from shiny import reactive
from shiny.express import input, render, ui
import palmerpenguins 
# load penguines data from palmerpenguins package into a data frame
df = palmerpenguins.load_penguins()

# create  penguins dashboard
ui.page_opts(title="Kamalini's Module 7 Penguins dashboard", fillable=True)

# create a sidebar with title Filter controls
with ui.sidebar(title="Dashboard Filter options"):
    # create a slider for mass between 2000 and 6000 with default 6000 selected
    ui.input_slider("mass", "Mass", 2000, 6000, 6000)
    # create multiple check boxes and select them
    ui.input_checkbox_group(
        "species",
        "Species",
        ["Adelie", "Gentoo", "Chinstrap"],
        selected=["Adelie", "Gentoo", "Chinstrap"],
    )

    # draw a horizontal line
    ui.hr()
    # create subheader named Links
    ui.h6("Resource Links")
    # create hyperlink for different things
    ui.a(
        "GitHub Source",
        href="https://github.com/S573647/cintel-07-tdash",
        target="_blank",
    )
    ui.a(
        "GitHub App",
        href="https://s573647.github.io/cintel-07-tdash/",
        target="_blank",
    )
    ui.a(
        "GitHub Issues",
        href="https://github.com/S573647/cintel-07-tdash/issues",
        target="_blank",
    )
    ui.a("PyShiny", href="https://shiny.posit.co/py/", target="_blank")
    ui.a(
        "Template: Basic Dashboard",
        href="https://shiny.posit.co/py/templates/dashboard/",
        target="_blank",
    )
    ui.a(
        "See also",
        href="https://shinylive.io/py/app/#h=0&code=NobwRAdghgtgpmAXGKAHVA6VBPMAaMAYwHsIAXOcpMASxlWICcyACVAG2LPewzgA9UjOAGcRLKONT8AOhABmjYjBYiAFjQi8BQ0eLoNmLTagCuZPC1M05i5ao1bj9Jq2EQAJnEaXhUQmQ0AG5wtkoq6prYAO40HgDmcGT6LkbuXowA+hxcPHIGrmxQnpISUh75qawicFAARkwQZaoQImH2qFDs8IyolPHWrc6GrJxQHtn9g20QcgDELGMebFOa4h5QZJJJcn0QA2uZHvIsALyLxOOT+9MAFACUcnLWWFCJmcSoybeB3HCnMjAAGlYF1NDQWAAFVZNAAimyggMeswgC3Gy2sqjicDqUEYcliZDUVhoGBE2NxjFun0oALANNmYHuiDkLDZJIwagATLdAQBlCl4pEsNEeZY1EieRZwELsFhqWoZFhkYhYryU1nszVshawpSoDzEaJNFWqODsOABCRkMiMGh1cxwFjajkmcyZGoWgI0ABecF5YE9looE02tvtjsBlkBACFiB5sCwALK1ESmYTwcjGJpJmjsdh0JLeNr4Z1NdkVytVivAQF1PPsTIW-ZEzIwGBR51gev5o5wL5qNsd0uA+QF9DeJv9Vvtzt1+PYNuSESZeKAgC69zLFZdCzdrHkTBYEFMMDq3hYxBO9daLpe+8yJ56NEIAZy3EXN8yJFM5DnYBjTQWAAYWIX8yE7LkAFZkR3csdRYQg-AoVQCwyO9SQfEQ0O8AManqRpMi-H8-xHACgNA8DOwAZksABGAAGBjLGg5FdxA5CnSgRCFUIABrBp+BYeIlFMVBszMVhTXkPMKEYZUFVUPpCBoUQMIwB9CF4gTiH4VdRNQPDlNUlcCxECCyL5c1gzgcVjLUkd4OrZyXJYWswAAQS8AtQjI4DHHMxg0H-ABxSgVWIDdLCDAJbNOdyvPNVT-38tZbWCsB10sTQCwgf4ABVGFMOA2KcisFmAziJB4y0dKEkSwPE-dlVVGT2DkhSnRobDigqJz7wgSTv20wT9MagNuvYXqm26izozAKyvRDYwes8Ocytcza2Xc-KmESRgakZebAJEEhfPmvVamHLKzSWuKdr24tKH-E6zv-S7YCi7NcoKoqSpddivOWbi1CYX1SC2OUiotFrOrVHEhX60k1CpUrypYIHqrUbA+kYXK+NhoknXJdVEYrF4oADEEYDBCAIQAJX7SLSxRuB5DpNQbVQEREAAel5+IaCJUw6gwEgYF5vkoIAdmogA2AAWaXeZU8hzQAWgY6j1b8b0Qk7LZGESMg6SIqaID4pEAachYPG6jgoETDYtmEu1galZ3uK2OoLQJIXiReKbsDAshv2IdhT1aB5EGcl1CQD0lCDxDxbnkUxe1O4RaUK4rmRdcnE+TzIFXGXDAWhG41hYeEXfy+pfaZfP2QAAXSbwME9zJFFgUINrZLwTjbrI9gOVpMm9i1o6bqthDIdMmjauTbKOBEHmnst445IOQ7DiOYCj5lt3ZTeXiTxgU7TjOkLgbO-rzvuOTPiYS4yAMK9H8Qa+4kK3ath-W8oBkDuCIu5BXgOvAeKxK5j09lPB+FZZ7zxYEPDAX8f5xFuJ7U4i9vDL1gfcXwRoPTWW9KQNs8Z-iAhgOnQIHBfJbieKiKEnAPzylmsQESsAHBGk0PECQ+YlKWhMn7Ikj9k6p3To2TON8ICnBziVFkSMxZFxfmXMAkIWE8BYAACXYZw4csEW5D2yJoxMR9+5szYCwkxZBo5snXogxgTRpCcj0WA1OslcETHwXgdeFZ+CnH3GSEhIZMhhjtA6CgDxfHwPZBAG8IhAmDXMFgUxRFNBh3AtEvx7ISCcEYHSEQ9kSwxK2r8C0dJ36DBYD2OUXgBxRhyWyKa552CJJAICGKoTwkRgoICGO-IQm2QxjaCJkYyIkQsgMsAlFSIAF9DFVnmCwKyBEnFsPMhwsB3DYj7H4XKIpQi1IQBPoXc+Eir5Z1kfI++BdlHn2LoqNRqyGjrN0Zs-Rf8XQAM8O3d8twugm0GWspo7yVSfMbk5SB+FXkQGLm42AcDnIaHMu+M4LQRCuNRSwjx7UvEry2NElgASgldOXj0yJ-oCE1LWEkySwSQXpLhZMh4izKworIO+YJodyn+nLjCauCI-7Itmlymood+AtPNAGRaNllgeVGb0+h68OViqSJkbAUr2ABlmRZNlCCkhINVSw9eyyNG5ETHyJONpvBovUDwvZXQDnFJEQne5F9JEemvrfXOii7lP0eaXKk5dTErOtXJd8XynI-IyCYi1LpIHvh4F6sMtqcW3OrI45x-AyThtwjg4Q3jV4EKacSuktS+wDiHI02JbJsB0jHDQCcWRmzxBnMOUpm08lMEKS6-ApbQYhCyNAeAdJJq9RrWUoWFT+R5t6Cwy8JxAICIADLTmJEETFLA4wJmTMuGplq+2dtclq9ppadzdgbJW9t-SuzLrlLCfsojbjtkeP22tlZRzjlxlOFsg5ZxIC7AAMW-ReNdf6WAvpgG+hZpqmHUXFHOu1oNdl8KdYIlSxzTnuouVI711y75+vZKfFRTzg1gGorCMNqb5LmtYFUoCX8o0VhjZOJN2AE2WNOjRzICG422IzTPQ16yXHcZtVkBDvIP0FrwcW49LkAnzgTEuMQq5J2bXrXWK99Sb3vq2j6BtoGW3rurXprt4ce2dKPQO4gQ7Hw9zHatCoZnXK8rpJR6j4nmFcEXduhce6xCWHvSwcDba1CWF6iwEDTbcYhfXepk99RzRno-RehoymaaqbXIB2M-mkz7tuPEN98mtpad7Dp-9w5pnBcfQOSDr6EtbS7I25tv6wumemdF5tcWINQZg6VZZ6shvDZG6Nsb42JuTam+rZZjN-CBBCIhLohB06bBoKQcQkW2byGDDMBY02DuHaO2NxhCxMbcV1gtp0Sd2AramoEUgsMC1w09ssmMTtLRMDW3somLA04QFIU0TeAD5vBDgJYaI13ihWBqHDf7gOnuePkr917TD8qKXhw9oHDYalQ-zMM6ICo8pDokE0ZqmP1tDFMDUZYppEh5SCihIkmxLzmEkjxYoiRMXLI8k4EO7PmesHqYA8Qj3fuXbB3938CPbhwAwPEDAlgZNFsJfcLcsQBHnisAaTYBOicvYRBz-YogMCMJB3rOXN3CByEgcrgllNBPIOE84mEK5jjABHtMI48h3KHMwyWdcGlyQQFuKS4pM1zKspYAAMigR-b37lx1rUykHzQofklkCD+bCYZkBP3HXC6MAcy8DgBHQgZAwgACO1gMzhUxWQfgZB8BEAhuFagnQSgzHY3IIv64gA",
        target="_blank",
    )

# create a row with multiple layout columns
with ui.layout_column_wrap(fill=False):
    # first column
    with ui.value_box(showcase=icon_svg("earlybirds")):
        "Number of penguins"

        @render.text
        def count():
            return filtered_df().shape[0]
    # second column
    with ui.value_box(showcase=icon_svg("ruler-horizontal")):
        "Average bill length"

        @render.text
        def bill_length():
            mean_length = filtered_df()['bill_length_mm'].mean()
            return f"{mean_length:.1f} mm"
    # third column
    with ui.value_box(showcase=icon_svg("ruler-vertical")):
        "Average bill depth"

        @render.text
        def bill_depth():
            return f"{filtered_df()['bill_depth_mm'].mean():.1f} mm"

# create a row with multiple columns
with ui.layout_columns():
    # first column
    with ui.card(full_screen=True):
        ui.card_header("Bill length and depth")

        @render.plot
        def length_depth():
            return sns.scatterplot(
                data=filtered_df(),
                x="bill_length_mm",
                y="bill_depth_mm",
                hue="species",
            )
    # second column
    with ui.card(full_screen=True):
        ui.card_header("Penguin data")

        @render.data_frame
        def summary_statistics():
            cols = [
                "species",
                "island",
                "bill_length_mm",
                "bill_depth_mm",
                "body_mass_g",
            ]
            return render.DataGrid(filtered_df()[cols], filters=True)


#ui.include_css(app_dir / "styles.css")

#Filter data at run time and display live results based on it.
@reactive.calc
def filtered_df():
    filt_df = df[df["species"].isin(input.species())]
    filt_df = filt_df.loc[filt_df["body_mass_g"] < input.mass()]
    return filt_df
