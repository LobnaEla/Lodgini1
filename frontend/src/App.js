import {Routes, Route} from 'react-router-dom';
import './App.css';
import Home from './componenets/home/home';
import About from './componenets/about';
import Signin from './componenets/sign/signin';
import Signup from './componenets/sign/signup';
import Signupowner from './componenets/sign/signupowner';
function App() {
  return (
    <div className="App">
      <Routes>
        <Route path='' element={<Home/>}/>
        <Route path='/about' element={<About/>}/>
        <Route path='/Sign_in' element={<Signin />}/>
        <Route path='/Sign_up' element={<Signup />}/>
        <Route path='/Sign_up_as_owner' element={<Signupowner />}/>
      </Routes>
    </div>
  );
}

export default App;
