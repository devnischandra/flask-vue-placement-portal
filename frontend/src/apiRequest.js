const BASE_URL = 'http://127.0.0.1:5000/api/v2'

export default async function apiRequest(endpoint,method,payload=null) {
    const url = BASE_URL + endpoint
    const token = localStorage.getItem("token")
    const options = {
        method: method,
        headers: {}
    }
    if(token){
        options.headers["Authorization"] = `Bearer ${token}`
    }
    if(payload){
        options.headers["Content-Type"] = "application/json"
        options.body = JSON.stringify(payload)
    }
    const response = await fetch(url,options)
    const data = await response.json()
    console.log(`${endpoint}`, data)
    
    return data
}
