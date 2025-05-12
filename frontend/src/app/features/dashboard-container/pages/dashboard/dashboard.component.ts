import { CommonModule } from '@angular/common';
import { Component, OnInit } from '@angular/core';
import { ChartModule } from 'primeng/chart';

@Component({
  selector: 'app-dashboard',
  imports: [CommonModule, ChartModule],
  templateUrl: './dashboard.component.html',
  styleUrl: './dashboard.component.scss',
})
export class DashboardComponent implements OnInit {
  summaryCards = [
    {
      title: 'Total Credit Limit',
      value: '$ 32,500.40',
      borderColorClass: 'border-l-green-600',
      textColorClass: 'text-green-600',
    },
    {
      title: 'Total Credit Used',
      value: '$ 23,500.36',
      borderColorClass: 'border-l-red-600',
      textColorClass: 'text-red-600',
    },
    {
      title: 'Utilization Rate',
      value: '64%',
      borderColorClass: 'border-l-blue-600',
      textColorClass: 'text-blue-600',
    },
    {
      title: 'Total Payment Due',
      value: '$ 3,560.40',
      borderColorClass: 'border-l-yellow-600',
      textColorClass: 'text-yellow-600',
    },
    {
      title: 'Next Due Date',
      value: '25/06/2025',
      borderColorClass: 'border-l-yellow-600',
      textColorClass: 'text-yellow-600',
    },
    {
      title: 'Last Transaction',
      value: '$ 2,400.00',
      borderColorClass: 'border-l-red-600',
      textColorClass: 'text-red-600',
    },
  ];

  data: any;
  options: any;

  ngOnInit(): void {
    const documentStyle = getComputedStyle(document.documentElement);
    const textColor = documentStyle.getPropertyValue('--p-text-color');
    const textColorSecondary = documentStyle.getPropertyValue(
      '--p-text-muted-color'
    );
    const surfaceBorder = documentStyle.getPropertyValue(
      '--p-content-border-color'
    );
    this.data = {
      labels: ['January', 'February', 'March', 'April', 'May', 'June'],
      datasets: [
        {
          label: 'Like U',
          backgroundColor: documentStyle.getPropertyValue('--p-cyan-500'),
          borderColor: documentStyle.getPropertyValue('--p-cyan-500'),
          data: [1230.2, 40.52, 1560, 5350.3, 1200, 500],
        },
        {
          label: 'BBVA',
          backgroundColor: documentStyle.getPropertyValue('--p-gray-500'),
          borderColor: documentStyle.getPropertyValue('--p-gray-500'),
          data: [1293.4, 2230, 4250, 300, 2450, 1000],
        },
      ],
    };
    this.options = {
      plugins: {
        legend: {
          labels: {
            color: textColor,
          },
        },
      },
      scales: {
        x: {
          ticks: {
            color: textColorSecondary,
            font: {
              weight: 500,
            },
          },
          grid: {
            color: surfaceBorder,
            drawBorder: false,
          },
        },
        y: {
          ticks: {
            color: textColorSecondary,
          },
          grid: {
            color: surfaceBorder,
            drawBorder: false,
          },
        },
      },
      onResize: (chart: any, size: any) => {
        console.log(chart);
        console.log(size);
      },
    };
  }
}
