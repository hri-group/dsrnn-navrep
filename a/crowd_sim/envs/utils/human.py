from a.crowd_sim.envs.utils.agent import Agent
from a.crowd_sim.envs.utils.state import JointState
from a.crowd_sim.envs.policy.orca import ORCA


class Human(Agent):
    def __init__(self, config, section):
        self.last_state = None
        super().__init__(config, section)

    def act(self, ob=None, global_map=None, local_map=None):
        """
        The state for human is its full state and all other agents' observable states
        :param ob:
        :return:
        """
        if ob is None:
            return self.policy.predict(self)
        state = JointState(self.get_full_state(), ob)
        if global_map is not None:
            action = self.policy.predict(state, global_map, self)
        elif local_map is not None:
            action = self.policy.predict(state, local_map, self)
        else:
            action = self.policy.predict(state)

        return action
