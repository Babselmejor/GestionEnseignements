import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CardSyllabusComponent } from './card-syllabus.component';

describe('CardSyllabusComponent', () => {
  let component: CardSyllabusComponent;
  let fixture: ComponentFixture<CardSyllabusComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [CardSyllabusComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(CardSyllabusComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
