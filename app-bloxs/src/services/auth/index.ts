export const Registry = async(body:any, setToken:any) => {
    
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
        let data:any = await resp.json();
        sessionStorage.setItem('token', data.user.token);
        setToken.setToken(data.user.token);
    });
}