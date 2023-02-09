import { Name, ImgProfile, Div } from './style'
import Profile from '../../assets/img/profile.jpeg';

const ProfileView = (props: any) => {
    return (
        <>
                <Div>
                    <ImgProfile src={Profile} width={60} height={60} draggable={false}/>  
                    <Name>Gabriel Menezes</Name>
                </Div>              
        </>
    )
}

export default ProfileView;