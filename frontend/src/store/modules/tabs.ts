

interface TabsState {
    tabs: Array<object>;
    activeKey: string
}

const TabsModule = {
    state: {
        tabs: [
            { title: '后台首页', key: '/home'}
        ],
        activeKey: "/home"
    } as TabsState,
    mutations: {
        addTab(state: TabsState, router) {
            state.tabs.push(router)
        },
        changeTabs(state: TabsState, tabs) {
            state.tabs = tabs
        },
        changeActiveKey(state: TabsState, key){
            state.activeKey = key
        }
    },
    actions: {},
    getters: {
        getTabs(state: TabsState) {
            return state.tabs
        },
        getActiveKey(state: TabsState){
            return state.activeKey
        }
    }
};

export default TabsModule;
