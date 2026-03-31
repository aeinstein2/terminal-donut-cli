#!/usr/bin/env python3
import argparse
import math
import sys
import time

SHADES = ".,-~:;=!*#$@"


def render_frame(a: float, b: float, width: int, height: int) -> str:
    zbuf = [0.0] * (width * height)
    out = [" "] * (width * height)

    # Torus parameters (classic ASCII donut)
    r1 = 1.0  # tube radius
    r2 = 2.0  # center radius
    k2 = 5.0  # distance from viewer

    # Scale to terminal size
    k1 = width * k2 * 3.0 / (8.0 * (r1 + r2))

    cos_a, sin_a = math.cos(a), math.sin(a)
    cos_b, sin_b = math.cos(b), math.sin(b)

    theta = 0.0
    while theta < 2 * math.pi:
        cost, sint = math.cos(theta), math.sin(theta)
        phi = 0.0
        while phi < 2 * math.pi:
            cosp, sinp = math.cos(phi), math.sin(phi)

            circlex = r2 + r1 * cost
            circley = r1 * sint

            # 3D rotation
            x = circlex * (cos_b * cosp + sin_a * sin_b * sinp) - circley * cos_a * sin_b
            y = circlex * (sin_b * cosp - sin_a * cos_b * sinp) + circley * cos_a * cos_b
            z = k2 + cos_a * circlex * sinp + circley * sin_a
            ooz = 1.0 / z

            xp = int(width / 2 + k1 * ooz * x)
            yp = int(height / 2 - (k1 * ooz * y) / 2)

            # Luminance
            l = (
                cosp * cost * sin_b
                - cos_a * cost * sinp
                - sin_a * sint
                + cos_b * (cos_a * sint - cost * sin_a * sinp)
            )

            idx = xp + yp * width
            if 0 <= xp < width and 0 <= yp < height and ooz > zbuf[idx]:
                zbuf[idx] = ooz
                shade_idx = int(max(0, min(len(SHADES) - 1, l * 8)))
                out[idx] = SHADES[shade_idx]

            phi += 0.07
        theta += 0.02

    rows = ["".join(out[i : i + width]) for i in range(0, width * height, width)]
    return "\n".join(rows)


def run(fps: int, frames: int | None, width: int, height: int) -> None:
    delay = 1.0 / max(1, fps)
    a = 0.0
    b = 0.0
    i = 0
    try:
        while frames is None or i < frames:
            frame = render_frame(a, b, width, height)
            sys.stdout.write("\x1b[H")
            sys.stdout.write(frame)
            sys.stdout.flush()
            a += 0.04
            b += 0.02
            i += 1
            time.sleep(delay)
    except KeyboardInterrupt:
        pass


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Render an animated ASCII donut in your terminal")
    p.add_argument("--fps", type=int, default=30, help="Frames per second (default: 30)")
    p.add_argument("--frames", type=int, default=None, help="Stop after N frames (default: infinite)")
    p.add_argument("--width", type=int, default=80, help="Frame width (default: 80)")
    p.add_argument("--height", type=int, default=24, help="Frame height (default: 24)")
    return p.parse_args()


def main() -> None:
    args = parse_args()
    # Clear screen once and hide cursor for cleaner animation
    sys.stdout.write("\x1b[2J\x1b[H\x1b[?25l")
    sys.stdout.flush()
    try:
        run(args.fps, args.frames, args.width, args.height)
    finally:
        # Show cursor again
        sys.stdout.write("\x1b[?25h\n")
        sys.stdout.flush()


if __name__ == "__main__":
    main()
