"""AiiDAlab QE plugin for Bader charge analysis."""

from aiidalab_qe.plugins import QeAppPlugin


class BaderPlugin(QeAppPlugin):
    @property
    def outline(self) -> str:
        return "Bader charge analysis"

    def structure_examples(self):
        from .structure_examples import structure_examples

        return structure_examples

    def configuration(self):
        from .model import BaderConfigurationSettingsModel
        from .setting import BaderConfigurationSettingPanel

        return {
            "panel": BaderConfigurationSettingPanel,
            "model": BaderConfigurationSettingsModel,
        }

    def resources(self):
        from .resources import BaderResourceSettingsModel, BaderResourceSettingsPanel

        return {
            "panel": BaderResourceSettingsPanel,
            "model": BaderResourceSettingsModel,
        }

    def workchain(self):
        from .workchain import workchain_and_builder

        return workchain_and_builder

    def result(self):
        from .result import BaderResultsModel, BaderResultsPanel

        return {
            "panel": BaderResultsPanel,
            "model": BaderResultsModel,
        }

    def guides(self):
        from pathlib import Path

        return {
            "title": self.outline,
            "path": Path(__file__).resolve().parent / "guides",
        }

    def metadata(self):
        return {
            "process_labels": {
                "QeBaderWorkChain": "Bader charge workflow",
                "PpCalculation": "Compute charge density",
                "BaderCalculation": "Compute Bader charge",
            }
        }
