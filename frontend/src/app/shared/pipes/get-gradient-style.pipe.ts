import { Pipe, PipeTransform } from '@angular/core';

@Pipe({
  name: 'getGradientStyle',
})
export class GetGradientStylePipe implements PipeTransform {
  transform(color: string): string {
    return `linear-gradient(0deg, ${color}, ${this.shadeColor(color, -20)})`;
  }

  private shadeColor(color: string, percent: number): string {
    let num = parseInt(color.slice(1), 16),
      amt = Math.round(2.55 * percent),
      R = (num >> 16) + amt,
      G = ((num >> 8) & 0x00ff) + amt,
      B = (num & 0x0000ff) + amt;

    return (
      '#' +
      (
        0x1000000 +
        (R < 255 ? (R < 0 ? 0 : R) : 255) * 0x10000 +
        (G < 255 ? (G < 0 ? 0 : G) : 255) * 0x100 +
        (B < 255 ? (B < 0 ? 0 : B) : 255)
      )
        .toString(16)
        .slice(1)
    );
  }
}
