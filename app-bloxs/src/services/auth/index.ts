export const Registry = async(body:any, setToken:any) => {
    
    body['birth'] = body['birth'] + 'T00:00:00'
    let authContent:any = JSON.stringify(body);

    await fetch(`http://localhost:5000/signup`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: authContent
    })
    .then(async(resp)=>{
        Login(body, setToken);
        
    });
}

export const Login = async(body: any, setToken: any) => {

    let authContent:any = JSON.stringify(body);

    await fetch(`http://localhost:5000/signin`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: authContent
    })
    .then(async(resp)=>{
        let response = await resp.json();        
        if (response.message != 'Sessão iniciada!') return Promise.reject(response.message);
        
        sessionStorage.setItem('token', response.user.token);
        sessionStorage.setItem('user_id', response.user.id);
        setToken(response.user.token);
    })
    .catch(err => {
        alert(err);
    })
}