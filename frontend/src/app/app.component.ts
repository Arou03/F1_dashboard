import * as Highcharts from 'highcharts';
import "highcharts/modules/treemap";
import { Component, OnInit, signal } from '@angular/core';
import { HighchartsChartComponent } from 'highcharts-angular';
import { BackendService } from './services/backend';
import { Classement } from './models/classement.model';
import { AppFormComponent, FormFieldConfig } from './components/app-form/app-form.component';
import { CommonModule } from '@angular/common';
import { MatProgressSpinnerModule } from '@angular/material/progress-spinner';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [HighchartsChartComponent, AppFormComponent, CommonModule, MatProgressSpinnerModule],
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {
  Highcharts: typeof Highcharts = Highcharts;
  chartOptions?: Highcharts.Options;
  ready = false;

  // Year field configuration for AppFormComponent
  formConfig: FormFieldConfig[] = [
    {
      type: 'select',
      label: 'Year',
      name: 'year',
      placeholder: 'Select a year',
      options: Array.from({ length: 6 }, (_, i) => {
        const year = 2020 + i;
        return { label: year.toString(), value: year };
      })
    }
  ];

  constructor(private backendService: BackendService) {}

  ngOnInit() {}

  // Called whenever the form emits a value change
  onFormChange(value: any) {
    if (value.year) {
      this.loadData(value.year);
    }
  }

  loadData(year: number) {
    this.ready = false;

    this.backendService.getClassement('team', year).subscribe((data: Classement[]) => {
      this.chartOptions = {
        title: { text: `Classement Teams ${year}` },
        series: [
          {
            type: 'treemap',
            data: data.map(d => ({ name: d.name, value: d.total_Points }))
          }
        ]
      };
      this.ready = true;
    });
  }
}
