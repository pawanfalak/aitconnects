import React from 'react' 
import {apiTweetCreate} from './lookup' 


export function TweetCreate(props){
    const TextAreaRef = React.createRef()
    const {didTweet} = props
    const handleBackendUpdate = (response, status) => {
      if(status === 201){
        didTweet(response)
      }else{
        console.log(response)
        alert("Error occured!!")
      }
    }
    const handleSubmit = (event) => {
        event.preventDefault()
        const newVal = TextAreaRef.current.value
        // baceend api request
        apiTweetCreate(newVal,handleBackendUpdate)
        TextAreaRef.current.value=''
    }
    return <div className={props.className}>
      <form onSubmit={handleSubmit}>
          <textarea ref={TextAreaRef} required={true} className='form-control' name='tweet'></textarea>
          <button type='submit' className='btn btn-primary my-3'>Tweet</button>
      </form>
  
    </div>
  }