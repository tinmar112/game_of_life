import argparse

def arguments() -> argparse.Namespace:

    DEFAULT_INITIAL_FILE = "game_of_life/patterns/glider.txt"
    DEFAULT_OUTPUT_FILE = "game_of_life/patterns/output.txt"
    DEFAULT_STEPS = 20
    DEFAULT_FPS = 10
    DEFAULT_WIDTH = 40
    MIN_W, MAX_W = 20, 80
    DEFAULT_HEIGHT = 30
    MIN_H, MAX_H = 20, 60

    parser = argparse.ArgumentParser(description = "Game of Life.",
                                     formatter_class = 
                                     argparse.ArgumentDefaultsHelpFormatter)
    
    parser.add_argument("--initial_file","-i",type=str,
                        default=DEFAULT_INITIAL_FILE,
                        help="File from which initial pattern will be loaded. ")
    
    parser.add_argument("--output_file","-o",type=str,
                        default=DEFAULT_OUTPUT_FILE,
                        help="File into which end position will be written.")
    
    parser.add_argument("--max","-m",type=int,
                        default=DEFAULT_STEPS,
                        help="Maximum number of steps to run.")
    
    parser.add_argument("--display","-d",
                        action="store_true",
                        help="Sets whether display should be on.")
    
    parser.add_argument("--fps","-f",type=int,
                        default=DEFAULT_FPS,
                        help="Number of FPS.")
    
    parser.add_argument("--width","-W",type=int,
                        default=DEFAULT_WIDTH,
                        help=f"Width of display window, between {MIN_W} an {MAX_W}")
    
    parser.add_argument("--height","-H",type=int,
                        default=DEFAULT_HEIGHT,
                        help=f"Height of display window, between {MIN_H} an {MAX_H}")

    args = parser.parse_args()

    if (args.width < MIN_W) or ((args.width > MAX_W)) or (args.height < MIN_H) or (args.height > MAX_H):
        raise ValueError
    
    else:
        return(args)