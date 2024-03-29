import React from "react";
import { Provider } from "react-redux";
import { BrowserRouter, Switch, Route } from "react-router-dom";
import Home from "./pages/Home";
import Login from "./pages/Login";
import Register from './pages/Register';
import CostumersList from './pages/CostumersList';
import store from './store'

class App extends React.Component{
  render() {
    return (
      <Provider store={ store }>
        <BrowserRouter>
        <Switch>
          <Route exact path="/" component={Home}/>
          <Route path="/login" component={Login}/>
          <Route path="/register" component={ Register } />
          <Route path="/costumers" component={ CostumersList } />
        </Switch>
        </BrowserRouter>
      </Provider>
    )
  }
}

export default App;