import React ,{ useState, useContext} from 'react';
import { UserContext } from '../../contexts/user';
import { AuthPage, AuthSide, WelcomeContainer, AuthTitle, AuthSubTitle, Form, 
  ActionButton, GoToLogin } from '../../styles/main-auth-structure';
import { Img } from './style'
import InputComponent from '../../components/Input/index';
import { Registry }from '../../services/auth/index'
import Logo from '../../assets/icon/infitity-bank-mark.svg';
import { useNavigate } from 'react-router-dom';
import { useEffect } from 'react';

const SignUp = () => {
  const { email, password, name, cpf, setToken, token, birth, setEmail, setPassword } = useContext(UserContext);

  const [loading, setLoading] = useState(false);

  const Auth = async () => {
    await Registry({email, password, name, cpf, birth}, setToken);
    
  }

  let navigate = useNavigate();

  useEffect(()=>{
    
    if (token.length > 0){
        navigate('/home')
    }
  })
  
  const routeChange = () =>{ 
    let path = `/signin`; 
    navigate(path);
  }

  return(
    <AuthPage>
      <AuthSide>
        <WelcomeContainer>
          <Img src={Logo}/>
          <AuthSubTitle>Cadastre-se</AuthSubTitle>
        </WelcomeContainer>
        <Form>
          <InputComponent inputType={'email'}/>
          <InputComponent inputType={'name'}/>
          <InputComponent inputType={'cpf'}/>
          <InputComponent inputType={'password'}/>
          <InputComponent inputType={'date'}/>
          <ActionButton type='button' onClick={Auth} disabled={false}>Criar Conta</ActionButton>
          <GoToLogin onClick={routeChange}>Já Tenho Conta</GoToLogin>
        </Form>
      </AuthSide>
    </AuthPage>
  )
}
export default SignUp;