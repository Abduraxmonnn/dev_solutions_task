hello_options = {
    1: "GET info about car",
    2: "Customization car",
    3: "Move",
    4: "Quit"
}


def type_options(color: str, door: str, engine: float, wheel: int) -> dict:
    return {
        1: f"Change color (current: {color})",
        2: f"Change door (current: {door})",
        3: f"Engine improvement (current: {engine})",
        4: f"Change wheel size (current {wheel})",
    }
