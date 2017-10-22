import React from 'react'

class ExampleWorkModal extends React.Component {



  render(){

    const example = this.props.example
    const modalClass = this.props.isOpen === true ? "modal--open" : "modal--closed"

    return(
      <div className={"background--skyBlue "+modalClass}>
        <span className="color--cloud modal__closeButton">
          <i className="fa fa-window-close-o" onClick={this.props.closeModal}></i>
        </span>
        <img alt="example screenshot of a project involving code"
             className="modal__image"
             src={example.image.src}/>
        <div className="color--cloud modal__text">
          <h2 className="modal__title">
            {example.title}
          </h2>
          <a className="color--skyBlue modal__link"
             href={example.href}>
            {example.href}
          </a>
          <p className="modal__description">
            {example.desc}
          </p>
        </div>
      </div>
    )
  }
}

export default ExampleWorkModal;
