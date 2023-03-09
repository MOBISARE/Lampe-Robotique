#ifndef LAMPE_HPP
#define LAMPE_HPP

#include "robot_dart/robot.hpp"

namespace robot_dart {
    namespace robots {

        class Lampe : public Robot {

        public:
            Lampe(const std::string& urdf = "lampe.urdf") : Robot(urdf)
            {
                fix_to_world();
                set_position_enforced(true);
            }

        };

    } // namespace robots
} // namespace robot_dart

#endif