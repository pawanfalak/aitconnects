import {backendLookup} from '../lookup'
export function apiTweetCreate(newData,callback){
    backendLookup("POST","/tweets/create/",callback,{content:newData})
}

export function apiTweetAction(tweetId, action, callback){
    const data = {id:tweetId, action:action}
    backendLookup("POST","/tweets/action/",callback,data)
}
  
export function apiTweetList(callback){
    backendLookup("GET","/tweets/",callback)
}