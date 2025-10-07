import { Component, Input, Output, EventEmitter } from '@angular/core';
import { FormGroup, FormControl, ReactiveFormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatInputModule } from '@angular/material/input';
import { MatSelectModule } from '@angular/material/select';
import { MatOptionModule } from '@angular/material/core';

export interface FormFieldConfig {
  type: 'input' | 'select';
  label: string;
  name: string;
  placeholder?: string;
  options?: { label: string; value: any }[];
}

@Component({
  selector: 'app-app-form',
  standalone: true,
  imports: [CommonModule, ReactiveFormsModule, MatFormFieldModule, MatInputModule, MatSelectModule, MatOptionModule],
  templateUrl: './app-form.component.html'
})
export class AppFormComponent {
  @Input() config: FormFieldConfig[] = [];
  @Output() formChange = new EventEmitter<any>();
  @Output() submit = new EventEmitter<any>();

  form: FormGroup = new FormGroup({});

  ngOnChanges() {
    const group: any = {};
    this.config.forEach(field => (group[field.name] = new FormControl('')));
    this.form = new FormGroup(group);

    // Emit changes whenever the form value changes
    this.form.valueChanges.subscribe(value => this.formChange.emit(value));
  }
}
