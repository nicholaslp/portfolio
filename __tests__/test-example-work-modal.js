import React from 'react'
import { configure, shallow } from 'enzyme';
import Adapter from 'enzyme-adapter-react-15';

import ExampleWorkModal from '../js/example-work-modal'

configure({ adapter: new Adapter() });

const thisExample = {
  'title': "Work Example 1",
  "href":"https://www.example.com",
  "desc":"Lorem ipsum",
  'image': {
    'desc': "Work Example 1",
    'src': "images/example1.png",
    'comment': "Work Example 1"
  }
};

describe("ExampleWorkModal Component", ()=> {


  const mockCloseModal = jest.fn()

  const component = shallow(<ExampleWorkModal example={thisExample} isOpen={false} closeModal={mockCloseModal}/>)
  const openComponent = shallow(<ExampleWorkModal example={thisExample} isOpen={true} closeModal={mockCloseModal}/>)

  const anchors = component.find('a')

  it("It should contain only one 'a' element", ()=>{
    expect(anchors.length).toEqual(1)
  })

  it("It should contain a link to our project", ()=>{
    expect(anchors.getElement().props.href).toEqual(thisExample.href)
  })

  it("Component in closed state should render with modal--closed css class", ()=>{
    expect(component.find(".background--skyBlue").hasClass("modal--closed")).toBe(true)
  })

  it("Component in open state should render with modal--open css class", ()=>{
    expect(openComponent.find(".background--skyBlue").hasClass("modal--open")).toBe(true)
  })

  it("Clicking the fa-window-close-o icon should trigger the close modal method", ()=> {
    openComponent.find('.fa-window-close-o').simulate('click')
    expect(mockCloseModal).toHaveBeenCalled()
  })

})
