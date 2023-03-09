#include <robot_dart/control/pd_control.hpp>
#include <robot_dart/robot_dart_simu.hpp>
#include <robot_dart/robots/lampe.hpp>


#ifdef GRAPHIC
#include <robot_dart/gui/magnum/graphics.hpp>
#endif

int main()
{
    std::cout << "Lampe is launching....." << std::endl;

    auto robot = std::make_shared<robot_dart::robots::Lampe>();
    robot->set_actuator_types("velocity");

    Eigen::VectorXd ctrl = robot_dart::make_vector({0.0, 0.0, 0.0, 0.0});

    auto controller = std::make_shared<robot_dart::control::PDControl>(ctrl);
    robot->add_controller(controller);

    robot_dart::RobotDARTSimu simu;
#ifdef GRAPHIC
    simu.set_graphics(std::make_shared<robot_dart::gui::magnum::Graphics>());
#endif
    simu.add_robot(robot);

    std::cout << robot->body_pose("head_link").translation().transpose() << std::endl;
    simu.run(1.0);

    ctrl << 0.0, 0.5, -0.5, 0.0;
    controller->set_parameters(ctrl);
    controller->set_pd(10., 0.);
    simu.run(2.0);

    std::cout << robot->body_pose("head_link").translation().transpose() << std::endl;

    return 0;
}