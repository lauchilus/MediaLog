import { AfterViewInit, Component, ElementRef, Input, OnInit, ViewChild } from '@angular/core';
import Swiper from 'swiper';
import { DescriptionPipe } from "../../pipes/description.pipe";
import { trigger, transition, style, animate } from '@angular/animations';
import 'swiper/css';
import { Navigation, Pagination } from 'swiper/modules';
import 'swiper/css/navigation';

@Component({
  selector: 'app-carrousel',
  standalone: true,
  templateUrl: './carrousel.component.html',
  styleUrl: './carrousel.component.css',
  imports: [DescriptionPipe,],
  animations: [
    trigger('fade', [
      transition('void => *', [
        style({ opacity: 0 }),
        animate(300, style({ opacity: 1 }))
      ])
    ])
  ]

})
export class CarrouselComponent implements OnInit, AfterViewInit {
[x: string]: any;
  @Input() contents: any[] = [];
  @Input() title!: string;
  @ViewChild('swiperContainer') swiperContainer!: ElementRef;
  selectedContent: string | null = null;
  private swiperInstance: Swiper | null = null;
  
  constructor() { }
  ngAfterViewInit(): void {
    this.initSwiper();
  }

  ngOnInit() {
  }

  private initSwiper() {
    this.swiperInstance =  new Swiper(this.swiperContainer.nativeElement, {
      modules: [Navigation],
      centeredSlides: false,
      direction: 'horizontal',
      loop: false,
      grabCursor: true,
      navigation: {
        nextEl: `.swiper-button-next-${this.title}`,
        prevEl: `.swiper-button-prev-${this.title}`,
      },
      breakpoints: {
        600: {
          slidesPerView: 2,
          slidesPerGroup: 2,
          spaceBetween: 5,
          centeredSlides: true,
        },
        900: {
          slidesPerView: 3,
          slidesPerGroup: 3,
          spaceBetween: 5,
          centeredSlides: true,
        },
        1200: {
          slidesPerView: 4,
          slidesPerGroup: 4,
          spaceBetween: 5,
          centeredSlides: false,
        },
        1500: {
          slidesPerView: 5,
          slidesPerGroup: 5,
          spaceBetween: 5,
          centeredSlides: false,
        },
        1800: {
          slidesPerView: 5,
          slidesPerGroup: 6,
          spaceBetween: 5,
          centeredSlides: false,
        }
      }
    })
  }

  setHoverElement(element: any) {
    this.selectedContent = element.title ?? element.name ?? element.node.title;
    console.log(element)
  }

  clearHoverElement() {
    this.selectedContent = null;
  }
}