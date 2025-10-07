import { provideHighcharts } from 'highcharts-angular';
import {ApplicationConfig} from '@angular/core';
import { provideHttpClient } from '@angular/common/http';

export const appConfig: ApplicationConfig = {
  providers: [
    provideHighcharts({
      // Optional: Define the Highcharts instance dynamically
      instance: () => import('highcharts'),

      // Global chart options applied across all charts
      options: {
        title: {
          style: {
            color: 'tomato'
          }
        },
        legend: {
          enabled: false
        }
      },

      // Include Highcharts additional modules (e.g., exporting, accessibility) or custom themes
      modules: () => {
        return [
          import('highcharts/esm/modules/accessibility'),
          import('highcharts/esm/modules/exporting'),
          import('highcharts/esm/modules/treemap'),
          import('highcharts/esm/themes/sunset')
        ]
      }
    }),
    provideHttpClient(),
  ]
};
