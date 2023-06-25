import {list} from "postcss";

interface UserState {
    token: null;
    username: string;
    real_name: string;
}

const UserModule = {
    state: {
        token: null,
        username: "",
        real_name: "",
        roles: [],
    } as UserState,
    mutations: {
        setUserInfo(state: UserState, user_info: object) {
            state.token = user_info.token
            state.username = user_info.username
            state.real_name = user_info.real_name
        }
    },
    actions: {},
    getters: {
        getToken(state: UserState) {
            return state.token
        },
        getRealName(state: UserState) {
            return state.real_name
        }
    }
};

export default UserModule;
