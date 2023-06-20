

interface CommonState {
    menuCollapsed: boolean;
    isSpinning: boolean
}

const CommonModule = {
    state: {
        menuCollapsed: false,
        isSpinning: false
    } as CommonState,
    mutations: {
        changeMenuCollapsed(state: CommonState) {
            state.menuCollapsed = !state.menuCollapsed
        },
        setLoading(state: CommonState, status: boolean) {
            state.isSpinning = status
        }
    },
    actions: {},
    getters: {
        getMenuCollapsed(state: CommonState) {
            return state.menuCollapsed
        },
        getIsSpinning(state: CommonState) {
            return state.isSpinning
        }
    }
};

export default CommonModule;
