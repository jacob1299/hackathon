import React, {useState} from 'react'
import { Center, Flex, Button, Input, Spacer } from '@chakra-ui/react'
import axios from 'axios'
import { useAuth0 } from '@auth0/auth0-react'
import { useForm } from 'react-hook-form'
import { Link, Route } from 'react-router-dom'

interface MainPageProps {
    isLoggedIn?: boolean
}

export const MainPage: React.FC<MainPageProps> = ({isLoggedIn}) => {
    const [data, setData] = React.useState<any[]>([])
    const { isAuthenticated, user } = useAuth0()
    const [postReturn, setPostReturn] = useState('Error: There was an issue')

    const userEmail = user?.email    
    const options = {
        headers: {
            'Access-Control-Allow-Headers': 'Origin, X-Requested-With, Content-Type, Accept'
        }
    }

    React.useEffect(() => {
        axios.get('http://34.75.42.233:5000/hello', options).then(res => setData(res.data)).catch(err => console.log(err))
    }, [])

    const {
        register,
        handleSubmit,
        formState: { errors }
      } = useForm()
    const onSubmit = (data: any) => axios.post(`http://34.75.42.233:5000/make_game?ante=${data.Ante}&color=${data.Color}&email=${userEmail}`).then((res) => setPostReturn(`https://${res.data.link}&user=${userEmail}`)).catch(err => console.log(err))
    console.log(errors) 
    console.log(postReturn)
    return (
        <Center>
            <Flex flexDirection='column'>
                <p style={{fontSize: '24px', color: '#094354', fontWeight: 'bold'}}>Select color and animal choice to begin matchmaking!</p>
                <Flex flexDirection='column' mt='6px' mx='2'>
                    <Center>
                        <form onSubmit={handleSubmit(onSubmit)}>
                        <Flex flexDirection='column' h='75px' w='300px'>
                            <select style={{height: '30px', color: 'black'}} {...register("Color", { required: true })}>
                                <option value="random">random</option>
                                <option value="white">white</option>
                                <option value="black">black</option>
                            </select>
                            <Spacer />
                            <select style={{height: '30px', color: 'black'}}{...register("Ante", { required: true })}>
                                <option value="none">none</option>
                                <option value="squirrel">squirrel</option>
                                <option value="swan">swan</option>
                                <option value="monkey">monkey</option>
                                <option value="lion">lion</option>
                                <option value="fox">fox</option>
                                <option value="tiger">tiger</option>
                                <option value="hyena">hyena</option>
                                <option value="shark">shark</option>
                                <option value="kangaroo">kangaroo</option>
                            </select>
                        </Flex>
                        <Input bg-color='teal.200' color='white.100' type='submit' mt='10px'/>
                        </form>
                    </Center>
                    {postReturn !== 'Error: There was an issue' && 
                    <Center>
                        <Button colorScheme='black' variant='solid' bgColor='teal.300' mt='8px'>
                            <a style={{color: 'brown'}} target='_blank' href={postReturn.replace('https', 'http')} rel='noopener noreferrer'>Take me to my game!</a>
                        </Button>
                    </Center>}
                </Flex>
            </Flex>
        </Center>
    )
}