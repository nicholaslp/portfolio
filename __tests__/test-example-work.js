import React from 'react'

import { configure, shallow } from 'enzyme';
import Adapter from 'enzyme-adapter-react-16';

configure({ adapter: new Adapter() });


import ExampleWork from '../js/example-work'

describe("Examplework Component", () => {

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

  let component = shallow(<ExampleWork work={myWork}/>)

  it("Should be a 'section' element", ()=> {
    console.log(component.debug())
  })

})
