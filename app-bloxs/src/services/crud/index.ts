export const GetById = async (endpoint: string, id: string, token: string, setItems: any) => {
    await fetch(`http://localhost:5000/${endpoint}/${id}`, {
        method: 'GET',
        headers: { 'Content-Type': 'application/json', 'token': token },
    })
    .then(async(resp)=>{
        let response = resp.json();
        setItems(response)
    });
}

export const GetFirstPage = async (endpoint: string, page: number, token: string, setItems: any) => {
    await fetch(`http://localhost:5000/${endpoint}/${page}`, {
        method: 'GET',
        headers: { 'Content-Type': 'application/json', 'token': token },
    })
    .then(async(resp)=>{
        let response = await resp.json();
        setItems(response[endpoint])
    });
}

export const Get = async (endpoint: string, token: string, setItems: any) => {
    await fetch(`http://localhost:5000/${endpoint}`, {
        method: 'GET',
        headers: { 'Content-Type': 'application/json', 'token': token },
    })
    .then(async(resp)=>{
        let response = await resp.json();
        console.log(response);
        
        setItems(response)
    });
}

export const Create = async(endpoint: string, token: string, body: any, functions: Array<any>) => {

    let authContent:any = JSON.stringify(body);

    await fetch(`http://localhost:5000/${endpoint}`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json', 'token': token },
        body: authContent
    })
    .then(async (resp: any)=>{
        let response = await resp.json();        
        if (response.message != 'ok') return Promise.reject(response.message);

        functions.forEach((_function) => {
            _function();
        })
        
    }).catch((err) => {
        alert(err);
    })
}

export const BlockAccount = async(token: string, functions: Array<any>) => {
    
    let body = { 'is_active': false }
    let authContent:any = JSON.stringify(body);

    await fetch(`http://localhost:5000/block`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json', 'token': token },
        body: authContent
    })

    .then(async(resp)=>{
        alert('Conta Bloqueada!')

    });
}