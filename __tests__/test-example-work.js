import React from 'react'

import { configure, shallow } from 'enzyme';
import Adapter from 'enzyme-adapter-react-16';

configure({ adapter: new Adapter() });


import ExampleWork, { ExampleWorkBubble } from '../js/example-work'

const myWork = [
  {
    'title': "Work Example 1",
    'image': {
      'desc': "Work Example 1",
      'src': "images/example1.png",
      'comment': "Work Example 1"
    }
  },
  {
    'title': "Work Example 2",
    'image': {
      'desc': "Serverless",
      'src': "images/example2.png",
      'comment': "A Serverless Portfolio"
    }
  },
]

describe("Examplework Component", () => {

  let component = shallow(<ExampleWork work={myWork} />);

  it("Should be a 'section' element", ()=> {
    expect(component.type()).toEqual('section')
  })

  it("Should contain as many ExampleWorkBubble elements as items in work array", ()=> {
    expect(component.find("ExampleWorkBubble").length).toEqual(myWork.length)
  })

})

describe("ExampleWorkBubble Component", () => {

  let component = shallow(<ExampleWorkBubble example={myWork[0]} />)

  let images = component.find("img")

  it("Should contain a single img element", ()=>{
    expect(images.length).toEqual(1)
  })

  it("Should have the image src set correctly", () => {
    expect(images.getElement().props.src).toEqual(myWork[0].image.src);
  });

})
